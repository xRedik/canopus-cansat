import os
import time
os.system("sudo pigpiod")
time.sleep(1)
import pigpio

pi = pigpio.pi()

class MotorControl:
  def __init__(self,esc_pin_A = None, esc_pin_B = None, esc_pin_C = None,
               esc_pin_D = None, min_value = 700, max_value = 2000):
    self.active_pins = []
    self.esc_pin_A = esc_pin_A
    self.esc_pin_B = esc_pin_B
    self.esc_pin_C = esc_pin_C
    self.esc_pin_D = esc_pin_D

    self.max_value = max_value
    self.min_value = min_value

    if self.esc_pin_A is not None:
      self.active_pins.append(self.esc_pin_A)
    if self.esc_pin_B is not None:
      self.active_pins.append(self.esc_pin_B)
    if self.esc_pin_C is not None:
      self.active_pins.append(self.esc_pin_C)
    if self.esc_pin_D is not None:
      self.active_pins.append(self.esc_pin_D)

    for pin in self.active_pins:
      pi.set_servo_pulsewidth(pin, 0)

  def manual_drive(self):
    print ("You have selected manual option so give a value between 0 and you max value")   
    while True:
      inp = input()
      if inp == "stop":
        self.stop()
        break
      elif inp == "control":
        self.control()
        break
      elif inp == "arm":
        self.arm()
        break
      else:
        for pin in self.active_pins:
          pi.set_servo_pulsewidth(pin, inp)

  def calibrate(self):
    for pin in self.active_pins:
      pi.set_servo_pulsewidth(pin, 0)

    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
       for pin in self.active_pins:
         pi.set_servo_pulsewidth(pin, max_value)
       print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
       inp = input()
       if inp == '':
           for pin in self.active_pins:
             pi.set_servo_pulsewidth(pin, min_value)
           print ("Wierd eh! Special tone")
           time.sleep(7)
           print ("Wait for it ....")
           time.sleep (5)
           print ("Im working on it, DONT WORRY JUST WAIT.....")
           for pin in self.active_pins:
             pi.set_servo_pulsewidth(pin, 0)
           time.sleep(2)
           print ("Arming ESC now...")
           for pin in self.active_pins:
             pi.set_servo_pulsewidth(pin, min_value)
           time.sleep(1)
           print ("See.... uhhhhh")
           self.control()

  def control(self):
    print ("I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'")
    time.sleep(1)
    speed = 900
    print ("Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed")
    while True:
      for pin in self.active_pins:
        pi.set_servo_pulsewidth(pin, speed)
      inp = input()
      if inp == "q":
          speed -= 100
          print ("speed = %d" % speed)
      elif inp == "e":
          speed += 100
          print ("speed = %d" % speed)
      elif inp == "d":
          speed += 10
          print ("speed = %d" % speed)
      elif inp == "a":
          speed -= 10
          print ("speed = %d" % speed)
      elif inp == "stop":
          self.stop()
          break
      elif inp == "manual":
          self.manual_drive()
            break
      elif inp == "arm":
          self.arm()
          break

  def arm(self):
    print ("Connect the battery and press Enter")
    inp = input()
    if inp == '':
      for pin in self.active_pins:
        pi.set_servo_pulsewidth(pin, 0)
      time.sleep(1)
      for pin in self.active_pins:
        pi.set_servo_pulsewidth(pin, max_value)
      time.sleep(1)
      for pin in self.active_pins:
        pi.set_servo_pulsewidth(pin, min_value)
      time.sleep(1)
      self.control()

  def stop():
    for pin in self.active_pins:
      pi.set_servo_pulsewidth(pin, 0)
    pi.stop()

