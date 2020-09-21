from picamera import PiCamera
from time import sleep
from PIL import Image

class Canopus_Camera:
  def __init__(self, resolution = (480,480), framerate = 15):
    try:
      self.camera = PiCamera()
      self.camera.resolution = resolution
      #self.camera.framerate = framerate
      self.status = False
      self.counter = 0
      self.send_pic_counter = 0
      self.camera_work = True
    except:
      self.camera_work = False

  def take_pic(self, filename = None):
    if self.camera_work:
      self.status = True
      self.camera.start_preview()
      sleep(2)
      self.camera.capture(filename)
      self.camera.stop_preview()
      self.counter += 1

  def comp_pic(self, filename = None, to_filename = None, optimate = True, quality = 95):
    if self.camera_work:
      compIm = Image.open(filename)
      compIm.save(to_filename, optimate = optimate, quality = quality)

  def take_and_comp_pic(self, filename = None, to_filename = None, optimate = True, quality = 95):
    if self.camera_work:
      self.status = True
      self.camera.start_preview()
      sleep(2)
      self.camera.capture(filename)
      self.camera.stop_preview()
      self.counter += 1
      compIm = Image.open(filename)
      compIm.save(to_filename, optimate = optimate, quality = quality)

