from .sd.rpm import CanRpm
from .sd.gps import CanGps
from .sd.batterylevel import CanBatLev
from .sd.altitude import read_altitude
from .sd.realang import CanGyroAcc
import time

start_time = time.time()

class Telemetry:
  def __init__(self,Team_ID = 6165, rpm_A_pin = None, rpm_B_pin = None, rpm_C_pin = None, rpm_D_pin = None,
               sea_lev_alt = 1004, num_pack = 0, gps_port = '/dev/ttyUSB0', hooker_object = None,
               camera_object = None):
    self.id = Team_ID
    self.gps = CanGps(port = gps_port)
    self.rpm_A = CanRpm(rpm_A_pin) if rpm_A_pin is not None else None
    self.rpm_B = CanRpm(rpm_B_pin) if rpm_B_pin is not None else None
    self.rpm_C = CanRpm(rpm_C_pin) if rpm_C_pin is not None else None
    self.rpm_D = CanRpm(rpm_D_pin) if rpm_D_pin is not None else None
    self.velo = CanGyroAcc()
    self.bl = CanBatLev()
    self.sea_lev_alt = sea_lev_alt
    self.num_pack = num_pack
    self.status_hooker = status_hooker
    self.time_model = 0
    self.hooker_start_time = 0
    self.start_status = True
    self.camera_object = camera_object
    self.hooker_object = hooker_object
  def full_tele_dict(self,elapsed_time = None):
    tel_dict = {}
    self.num_pack += 1
    self.time_model = time.time() - start_time
    if self.hooker_object.status and self.start_status:
      self.hooker_start_time = time.time()
      self.start_status = False
    tel_dict['Team_ID'] = self.id
    tel_dict['working_time'] = '{:.2f}'.format(self.time_model)
    tel_dict['number_of_pocket'] = self.num_pack
    tel_dict['bat_lev'], tel_dict['voltage'] = self.bl.battery_level_voltage()
    tel_dict['altitude'] = read_altitude(self.sea_lev_alt)
    tel_dict['velocity'] = self.velo.read_velocity(elapsed_time) if elapsed_time is not None else None
    tel_dict['lat'], tel_dict['lng'] = self.gps.read_gps()
    tel_dict['cap_pic'] = self.camera_object.status
    tel_dict['rpm_1'] = self.rpm_A.read_rpm() if self.rpm_A is not None else None
    tel_dict['rpm_2'] = self.rpm_B.read_rpm() if self.rpm_B is not None else None
    tel_dict['rpm_3'] = self.rpm_C.read_rpm() if self.rpm_C is not None else None
    tel_dict['rpm_4'] = self.rpm_D.read_rpm() if self.rpm_D is not None else None
    tel_dict['time_after_sep'] = '{:.2f}'.format(time.time() - self.hooker_start_time) if self.hooker_object.status else 0.0
    tel_dict['numb_of_pic'] = self.camera_object.counter
    tel_dict['send_pic'] = self.camera_object.send_pic_counter
    return tel_dict
