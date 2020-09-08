import time
import board
import busio
import adafruit_mpu6050
import math

class CanAng():
  def __init__(self,address = '0x68', ACCELEROMETER_SENSITIVITY = 8192.0,
               GYROSCOPE_SENSITIVITY = 65.536, dt = 0.01, M_PI = 3.14159265359):
    self.address = address
    self.ACCELEROMETER_SENSITIVITY = ACCELEROMETER_SENSITIVITY
    self.GYROSCOPE_SENSITIVITY = GYROSCOPE_SENSITIVITY
    self.dt = dt
    self.M_PI = M_PI
    try:
      i2c = busio.I2C(board.SCL, board.SDA)
      self.mpu = adafruit_mpu6050.MPU6050(i2c)
    except:
      self.mpu = None
  def acc(self):
    if self.mpu is not None:
      acc_x, acc_y, acc_z = self.mpu.acceleration
      return {'acc_x':acc_x, 'acc_y':acc_y, 'acc_z':acc_z}
    return None
  def gyro(self):
    if self.mpu is not None:
      gyro_x, gyro_y, gyro_z = self.mpu.gyro
      return {'gyro_x':gyro_x, 'gyro_y':gyro_y, 'gyro_z':gyro_z}
    return None
  def complementary_filter(self,pitch = 3,roll = 3):
    if self.mpu is not None:
      gyro_x, gyro_y, gyro_z = self.mpu.gyro
      acc_x, acc_y, acc_z = self.mpu.acceleration
      pitch += gyro_x * self.dt
      roll -= gyro_y * self.dt
      #pitch += (gyro_x / self.GYROSCOPE_SENSITIVITY) * self.dt
      #roll -= (gyro_y / self.GYROSCOPE_SENSITIVITY) * self.dt
      forceMagApp = abs(acc_x) + abs(acc_y) + abs(acc_y)
      if forceMagApp > 8192 and forceMagApp < 32768:
        pitchAcc = math.atan2(acc_y, acc_z) * 180 / self.M_PI
        pitch = pitch * 0.98 + pitchAcc * 0.02
        rollAcc = math.atan2(acc_x, acc_z) * 180 / self.M_PI
        roll = roll * 0.98 + rollAcc * 0.02
      return pitch, roll
