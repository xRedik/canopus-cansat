from picamera import PiCamera
from time import sleep
from PIL import Image


def canopusTakePic():
	camera.start_preview()
	sleep(5)
	camera.capture('/home/pi/Desktop/Programs/Camera/image2.jpg') #it will change
	camera.stop_preview()

def canopusCompPic():
	compIm=Image.open('/home/pi/Desktop/Programs/Camera/image2.jpg')
	compIm.save("/home/pi/Desktop/Programs/Camera/image2Comp.jpg",optimate=True,quality=95)

camera = PiCamera()
camera.resolution = (480, 480)
camera.framerate = 15

canopusTakePic()
canopusCompPic()
