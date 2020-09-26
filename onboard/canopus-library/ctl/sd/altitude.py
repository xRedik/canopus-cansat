import board
import busio
import adafruit_bmp280

class Altitude:
  def __init__(self, slp = 1020):
    try:
      self.i2c = busio.I2C(board.SCL, board.SDA)
      self.sensor = adafruit_bmp280.Adafruit_BMP280_I2C(self.i2c, address = 0x76)
      self.sensor.sea_level_pressure = slp
    except:
      self.sensor = None
    self.previous_altitude = 0
    self.current_altitude = 0
    self.velocity = 0
  def read_altitude(self):
    if self.sensor is not None:
      self.previous_altitude = self.current_altitude
      self.current_altitude = self.sensor.altitude
      return '{0:.3f}'.format(self.current_altitude)
    return None
  def read_velocity(self, elapsed_time = 1):
    _ = self.read_altitude()
    self.velocity = '{:.3f}'.format(abs((self.current_altitude - self.previous_altitude) / elapsed_time)) if self.sensor is not None else None
    return self.velocity

