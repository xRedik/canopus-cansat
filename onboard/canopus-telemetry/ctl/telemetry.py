from .rpm import CanRpm
#from .gps import canopus_gps
from .batterylevel import CanBatLev
from .altitude import read_altitude
import time

start_time = time.time()
tel_dict = {}
rpm_1 = CanRpm(27)
#rpm_2 = CanRpm(18)
#rpm_3 = CanRpm(19)
#rpm_4 = CanRpm(20)
bl = CanBatLev()

def func_for_tele_dict():
  tel_dict['Team_ID'] = 6169
  tel_dict['working_time'] = '{:.2f}'.format(time.time() - start_time)
  tel_dict['number_of_pocket'] = None
  tel_dict['bat_lev'], _ = bl.battery_level_voltage()
  tel_dict['altitude'] = read_altitude(1010)
  tel_dict['velocity'] = None
  #tel_dict['lat'], tel_dict['lng'] = canopus_gps()
  tel_dict['cap_pic'] = None #boolean
  tel_dict['rpm_1'] = rpm_1.read_rpm()
  #tel_dict['rpm_2'] = rpm_2.read_rpm()
  #tel_dict['rpm_3'] = rpm_3.read_rpm()
  #tel_dict['rpm_4'] = rpm_4.read_rpm()
  tel_dict['time_after_sep'] = None
  tel_dict['numb_of_pic'] = None
  tel_dict['send_pic'] = None
  return tel_dict

