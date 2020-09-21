from ctl.telemetry import Telemetry
from time import sleep
from ctl.mc.hooker import Hooker


hooker = Hooker(servo_pin = 17)

tele = Telemetry(sea_lev_alt = 1020, rpm_A_pin = 27, gps_port = '/dev/ttyUSB2',
                 status_hooker = hooker.status)


while True:
  tel_dict = tele.full_tele_dict()
  tele.status_hooker = hooker.status
  hooker.open_servo()
  for name in tel_dict:
    print(name + ": " + str(tel_dict[str(name)]))
  print("\n")
  sleep(1)
