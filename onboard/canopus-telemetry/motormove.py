from ctl.motorcontrol import MotorControl

motors = MotorControl(esc_pin_A = 17, esc_pin_B = 27,
                      esc_pin_C = 22, esc_pin_D = 21)

motors.calibrate()
