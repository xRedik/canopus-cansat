import RPi.GPIO as GPIO
import time

class Hooker:
  def __init__(self,servo_pin = None, status = False):
    self.servo_pin = servo_pin
    if self.servo_pin is not None:
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.servo_pin, GPIO.OUT)
      self.hooker = GPIO.PWM(servo_pin, 50)
      self.hooker.start(2.5)
    self.status = status
  def set_angle(self,angle):
    if self.servo_pin is not None:
      duty = angle / 18 + 2
      self.hooker.ChangeDutyCycle(duty)
      time.sleep(0.2)
  def open_servo(self):
    self.set_angle(27)
    self.status = True
    return self.status
  def close_servo(self):
    self.set_angle(150)
    self.status = False
    return self.status
  def pass_servo(self):
    self.set_angle(130)
    self.status = False
    return self.status
  def clean_pin(self):
    if self.servo_pin is not None:
      self.hooker.stop()
      GPIO.cleanup()
