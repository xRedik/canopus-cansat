import board
import busio
import adafruit_bmp280
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

#sensor.sea_level_pressure = 1013.25 It will change
sensor.sea_level_pressure = 1004 #Prosta prob

while True:
	print('Temperature: {0:.3f} degrees C'.format(sensor.temperature))
	print('Pressure: {0:.3f} hPa'.format(sensor.pressure))

	print('Altitude: {0:.3f} meters\n'.format(sensor.altitude))
	time.sleep(3)
