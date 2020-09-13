import time
import board
import busio
import adafruit_mpu6050
import math

class CanGyroAcc():
  def __init__(self,address = '0x68', pitch = 0, roll = 0, rad_to_deg = 180/3.14159265359, initial_speed = 0):
    self.address = address
    self.rad_to_deg = rad_to_deg
    self.pitch = pitch
    self.roll = roll
    self.initial_speed = initial_speed
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
  def complementary_filter(self, elapsed_time):
    if self.mpu is not None:
      gyro_x, gyro_y, gyro_z = self.mpu.gyro
      acc_x, acc_y, acc_z = self.mpu.acceleration
      acc_x, acc_y, acc_z = acc_x / 9.80665, acc_y / 9.80665, acc_z / 9.80665
      acc_ang_x = math.atan(acc_y / math.sqrt(pow(acc_x, 2) + pow(acc_z,2))) * self.rad_to_deg
      acc_ang_y = math.atan(-1 * acc_x / math.sqrt(pow(acc_y,2) + pow(acc_z,2))) * self.rad_to_deg

      self.roll = 0.98 * (self.roll + gyro_x * elapsed_time) + 0.02 * acc_ang_x
      self.pitch = 0.98 * (self.pitch + gyro_y * elapsed_time) + 0.02 * acc_ang_y
      return self.pitch, self.roll
  def read_velocity(self,elapsed_time):
    if self.mpu is not None:
      acc_x, acc_y, acc_z = self.mpu.acceleration
      self.initial_speed = self.initial_speed + elapsed_time * math.sqrt(pow(acc_x,2) + pow(acc_y,2) + pow(acc_z,2))
      return self.initial_speed
