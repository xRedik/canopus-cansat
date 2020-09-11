import ..ctl.angle import angle

class CanPid():
  def __init__(kp = 0, kd = 0, ki = 0, des_val = 0):
    self.kp = kp
    self.kd = kd
    self.ki = ki
    self.des_val = des_val


