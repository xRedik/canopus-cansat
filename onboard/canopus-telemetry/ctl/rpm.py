#!/usr/bin/env python3

import pigpio
from .read_RPM import reader
import RPi.GPIO as GPIO

pi = pigpio.pi()

class CanRpm():
  def __init__(self,pin):
    self.gpio = pin
    self.tach = reader(pi,self.gpio)
  def read_rpm(self):
    return '{:.2f}'.format(self.tach.RPM())
