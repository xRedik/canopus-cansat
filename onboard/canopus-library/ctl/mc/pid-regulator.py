import ..ctl.angle import angle

class CanPid():
  def __init__(self, kp_pitch = 0, kd_pitch = 0, ki_pitch = 0, des_pitch_val = 0,
                     kp_roll = 0,  kd_roll = 0,  ki_roll = 0,  des_roll_val = 0):
    self.kp_pitch = kp_pitch
    self.kd_pitch = kd_pitch
    self.ki_pitch = ki_pitch
    self.pid_pitch_p = 0
    self.pid_pitch_i = 0
    self.pid_pitch_d = 0
    self.PID_pitch = 0
    self.des_pitch_val = des_pitch_val
    self.previous_pitch_error = 0

    self.kp_roll = kp_roll
    self.kd_roll = kd_roll
    self.ki_roll = ki_roll
    self.pid_roll_p = 0
    self.pid_roll_i = 0
    self.pid_roll_d = 0
    self.PID_roll = 0
    self.des_roll_val = des_roll_val
    self.previous_roll_error = 0

  def pitch_regulator(self,pitch = 0, elapsed_time = 0, throttle = 1000):
    error = pitch - self.des_pitch_val
    self.pid_pitch_p = self.kp_pitch * error
    if abs(error) < 3:
      self.pid_pitch_i = self.pid_pitch_i + (self.ki_pitch * error)
    self.pid_pitch_d = self.kd_pitch * ((error - self.previous_pitch_error)/elapsed_time)
    self.PID_pitch =  self.pid_pitch_p + self.pid_pitch_i + self.pid_pitch_d
    if self.PID_pitch < -1000:
      self.PID_pitch = - 1000
    elif self.PID_pitch > 1000L
      self.PID_pitch = 1000
    pwm_left = throttle + self.PID_pitch
    pwm_right = throttle - self.PID_pitch
    self.previous_pitch_error = error
    return pwm_left, pwm_right

  def roll_regulator(self,roll = 0, elapsed_time = 0, throttle = 1000):
    error = roll - self.des_roll_val
    self.pid_roll_p = self.kp_roll * error
    if abs(error) < 3:
      self.pid_roll_i = self.pid_roll_i + (self.ki_roll * error)
    self.pid_roll_d = self.kd_roll * ((error - self.previous_roll_error)/elapsed_time)
    self.PID_roll =  self.pid_roll_p + self.pid_roll_i + self.pid_roll_d
    if self.PID_roll < -1000:
      self.PID_roll = - 1000
    elif self.PID_roll > 1000:
      self.PID_roll = 1000
    pwm_front = throttle + self.PID_roll
    pwm_back = throttle - self.PID_roll
    self.previous_roll_error = error
    return pwm_front, pwm_back

