#!/usr/bin/env python3

import pigpio
from .read_RPM import reader
import RPi.GPIO as GPIO
import numpy as np

pi = pigpio.pi()

class CanRpm():
  def __init__(self,pin):
    self.gpio = pin
    self.tach = reader(pi,self.gpio)
    self.rpm = 0
  def read_rpm(self):
    self.rpm = np.ushort('{:.2f}'.format(self.tach.RPM()))
    return self.rpm

