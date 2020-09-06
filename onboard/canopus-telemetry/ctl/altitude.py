import board
import busio
import adafruit_bmp280

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

def read_altitude(slp):
  sensor.sea_level_pressure = slp #1004
  return '{0:.3f}'.format(sensor.altitude)
