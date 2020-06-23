import serial
import time
import string
import pynmea2

boolGps=False

def CanopusGPS():
    global boolGps
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline().decode('utf-8')
    if newdata[0:6] == "$GPRMC":
        boolGps=True
        newmsg=pynmea2.parse(newdata)
        lat=str(newmsg.latitude)
        lng=str(newmsg.longitude)
        return lat,lng
    boolGps=False
    return 0,0

port="/dev/ttyUSB0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)

while True:
    lat,lng=CanopusGPS()
    if(boolGps):
        gps = "Latitude = " + str(lat) + " and Longitude = " + str(lng)
        print(gps)
    
