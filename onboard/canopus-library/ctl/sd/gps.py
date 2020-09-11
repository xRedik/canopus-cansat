#!/usr/bin/env python3

#Altitude is possible
#Yoxlamaga axot yoxdu

import serial
import time
import string
import pynmea2

class CanGps():
  def __init__(self, port = '/dev/ttyUSB0'):
    self.port = port
    try:
      self.ser=serial.Serial(self.port, baudrate=9600, timeout=0.5)
    except:
      self.ser = None

  def read_gps(self):
    try:
      dataout = pynmea2.NMEAStreamReader()
      newdata=self.ser.readline().decode('utf-8')
      if newdata[0:6] == "$GPRMC":
        newmsg=pynmea2.parse(newdata)
        lat=str(newmsg.latitude)
        lng=str(newmsg.longitude)
        return lat,lng
      return 0,0
    except:
      return -1,-1
