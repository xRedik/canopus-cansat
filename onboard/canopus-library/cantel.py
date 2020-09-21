from ctl.telemetry import Telemetry
from time import sleep
from ctl.mc.hooker import Hooker
from ctl.cm.camera import Canopus_Camera

hooker = Hooker(servo_pin = 17)
camera = Canopus_Camera()

tele = Telemetry(sea_lev_alt = 1010, rpm_A_pin = 27, gps_port = '/dev/ttyUSB2',
                 hooker_object = hooker, camera_object = camera)

while True:
  tel_dict = tele.full_tele_dict()
  hooker.open_servo()
  for name in tel_dict:
    print(name + ": " + str(tel_dict[str(name)]))
  print("\n")
  sleep(1)
