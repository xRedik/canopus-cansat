from ctl.telemetry import Telemetry
from time import sleep
from ctl.mc.hooker import Hooker
from ctl.cm.camera import Canopus_Camera
import time

curr_time = time.time()

hooker = Hooker(servo_pin = 17)
camera = Canopus_Camera()

tele = Telemetry(sea_lev_alt = 1020, rpm_A_pin = 27, gps_port = '/dev/ttyUSB2',
                 hooker_object = hooker, camera_object = camera)

while True:
  prev_time = curr_time
  curr_time = time.time()
  elapsed_time = curr_time - prev_time
  tel_dict = tele.full_tele_dict(elapsed_time = elapsed_time)
  #hooker.open_servo()
  for name in tel_dict:
    print(name + ": " + str(tel_dict[str(name)]))
  print("\n")
  sleep(1)
