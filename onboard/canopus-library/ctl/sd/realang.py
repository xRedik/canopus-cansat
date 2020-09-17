import time
import board
import busio
import adafruit_mpu6050
import math

class CanAng():
  def __init__(self,address = '0x68', pitch = 0, roll = 0, rad_to_deg = 180/3.14159265359):
    self.address = address
    self.rad_to_deg = rad_to_deg
    self.pitch = pitch
    self.roll = roll
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
  def complementary_filter(self, elapsedTime):
    if self.mpu is not None:
      gyro_x, gyro_y, gyro_z = self.mpu.gyro
      acc_x, acc_y, acc_z = self.mpu.acceleration
      acc_x, acc_y, acc_z = acc_x / 9.80665, acc_y / 9.80665, acc_z / 9.80665
      acc_ang_x = math.atan(acc_y / math.sqrt(pow(acc_x, 2) + pow(acc_z,2))) * self.rad_to_deg
      acc_ang_y = math.atan(-1 * acc_x / math.sqrt(pow(acc_y,2) + pow(acc_z,2))) * self.rad_to_deg

      self.roll = 0.98 * (gyro_x * elapsedTime) + 0.02 * acc_ang_x
      self.pitch = 0.98 * (gyro_y * elapsedTime) + 0.02 * acc_ang_y
      return self.pitch, self.roll
