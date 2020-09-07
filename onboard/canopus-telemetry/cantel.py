from ctl.telemetry import func_for_tele_dict
from time import sleep

while True:
  tel_dict = func_for_tele_dict()
  for name in tel_dict:
    print(name + ": " + str(tel_dict[str(name)]))
  print("\n")
  sleep(2)
