#!/usr/bin/env python3

#Altitude is possible
#Yoxlamaga axot yoxdu

import serial
import time
import string
import pynmea2

port="/dev/ttyUSB0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)

def canopus_gps():
  dataout = pynmea2.NMEAStreamReader()
  newdata=ser.readline().decode('utf-8')
  try:
    if newdata[0:6] == "$GPRMC":
      newmsg=pynmea2.parse(newdata)
      lat=str(newmsg.latitude)
      lng=str(newmsg.longitude)
      return lat,lng
  except:
    return 0,0
