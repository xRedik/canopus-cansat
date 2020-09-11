from ctl.telemetry import Telemetry
from time import sleep

tele = Telemetry(sea_lev_alt = 1010, rpm_A_pin = 27, gps_port = '/dev/ttyUSB2')


while True:
  tel_dict = tele.full_tele_dict()
  for name in tel_dict:
    print(name + ": " + str(tel_dict[str(name)]))
  print("\n")
  sleep(1)
