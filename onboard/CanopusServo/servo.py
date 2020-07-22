import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

hooker = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
hooker.start(2.5) # Initialization

def set_angle(angle):
	duty = angle / 18 + 2
	hooker.ChangeDutyCycle(duty)
	time.sleep(0.2)

try:
	while True:
		set_angle(54)
		set_angle(90)
		set_angle(120)
		set_angle(180)
		set_angle(150)
		set_angle(90)
		set_angle(50)
		set_angle(30)
except KeyboardInterrupt:
	hooker.stop()
	GPIO.cleanup()

