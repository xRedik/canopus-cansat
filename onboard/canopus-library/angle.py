from ctl.sd.realang import CanAng
import time

sensor_angle = CanAng()

time_main = time.time()

while True:
  time_prev = time_main
  time_main = time.time()
  elapsed_time = time_main - time_prev
  pitch, roll = sensor_angle.complementary_filter(elapsed_time)
  print("pitch is " + str(pitch))
  print("roll is " + str(roll))
  time.sleep(1)
