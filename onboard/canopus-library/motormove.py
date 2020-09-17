from ctl.mc.motorcontrol import MotorControl

motors = MotorControl(esc_pin_A = 26, esc_pin_B = 19,
                      esc_pin_C = 13, esc_pin_D = 6)

motors.control()
