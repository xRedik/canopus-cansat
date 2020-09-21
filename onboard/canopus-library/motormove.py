from ctl.mc.motorcontrol import MotorControl

motors = MotorControl(esc_pin_A = 16, esc_pin_B = 20, esc_pin_C = 21)


motors.calibrate()
