from ctl.sd.altitude import Altitude
import time

current_time = time.time()

altitude = Altitude(slp = 1020)

while 1:
  start_time = current_time
  current_time = time.time()
  elapsed_time = current_time - start_time
  #print(elapsed_time)
  print(altitude.read_velocity(elapsed_time = elapsed_time))
  time.sleep(0.5)
  altitude_numb = altitude.read_altitude()
  #print("Current Altitude is " + str(altitude.current_altitude))
  #print("Previous Altitude is " + str(altitude.previous_altitude))
