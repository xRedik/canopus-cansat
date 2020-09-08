from ctl.sd.realang import CanAng
import time

sensor_angle = CanAng()

pitch, roll = sensor_angle.complementary_filter()
while True:
  pitch, roll = sensor_angle.complementary_filter(pitch,roll)
  print("pitch is " + str(pitch))
  print("roll is " + str(roll))
  #print(sensor_angle.acc())
  #print()
  #print(sensor_angle.gyro())
  time.sleep(1)
