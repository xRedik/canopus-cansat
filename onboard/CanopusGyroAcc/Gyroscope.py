import time
import board
import busio
import adafruit_mpu6050

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    acc_x,acc_y,acc_z =mpu.acceleration
    gyro_x, gyro_y, gyro_z = mpu.gyro
    #Bu ikisini dustura gore birlesdirib total angle tapmaq lazimdi. Axot yoxdu
    print("Acceleration: X: %.2f Y: %.2f Z: %.2f m/s^2" %(acc_x,acc_y,acc_z))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees\n" % (gyro_x,gyro_y,gyro_z))
    time.sleep(1)
