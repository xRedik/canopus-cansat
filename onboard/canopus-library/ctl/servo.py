import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

hooker = GPIO.PWM(servoPIN, 50)
hooker.start(2.5)

def set_angle(angle):
	duty = angle / 18 + 2
	hooker.ChangeDutyCycle(duty)
	time.sleep(0.2)

try:
	while True:
		set_angle(130) #rezin acmaq
		#set_angle(27) #acmaq tam
		#set_angle(150) #tam baglamaq
except KeyboardInterrupt:
	hooker.stop()
	GPIO.cleanup()

