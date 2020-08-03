import time
import board
import busio
import adafruit_mpu6050
import adafruit_bmp280

i2c = busio.I2C(board.SCL,board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

bmp.sea_level_pressure = 1005

while True:
	acc_x, acc_y, acc_z = mpu.acceleration
	gyro_x, gyro_y, gyro_z = mpu.gyro
	print("*******Gyro_Acc*******")
	print("Acc: X: %.2f Y: %.2f Z: %.2f m/s^2" %(acc_x,acc_y,acc_z))
	print("Gyro: X: %.2f Y: %.2f Z: %.2f degrees\n\n" %(gyro_x,gyro_y,gyro_z))
	print("*******Altitude*******")
	print("Altitude: %.2f meters\n\n" %(bmp.altitude))
	time.sleep(2)
