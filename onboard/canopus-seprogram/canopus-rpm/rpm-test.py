#!/usr/bin/env python3

import pigpio
from read_RPM import reader
import RPi.GPIO as GPIO
from time import sleep

pi = pigpio.pi()

RPM_GPIO = 27
SAMPLE_TIME = 1
tach = reader(pi,RPM_GPIO)


while 1:
  try:
    rpm = '{:.2f}'.format(tach.RPM())
    print(rpm)
    sleep(SAMPLE_TIME)
  except Exception as e:
    print(e)
    sleep(5)
