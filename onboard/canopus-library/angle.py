from ctl.sd.realang import CanGyroAcc
import time

sensor_angle = CanGyroAcc()

time_main = time.time()

while True:
  time_prev = time_main
  time_main = time.time()
  elapsed_time = time_main - time_prev
  #print(elapsed_time)
  pitch, roll = sensor_angle.complementary_filter(elapsed_time)
  #print(sensor_angle.gyro())
  #print(sensor_angle.acc())
  #print("pitch is " + str(pitch))
  #print("roll is " + str(roll))
  velocity = sensor_angle.read_velocity(elapsed_time)
  print(velocity)
  time.sleep(0.1)
