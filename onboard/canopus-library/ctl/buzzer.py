from gpiozero import Buzzer
import time

buzzer = Buzzer(17)

while True:
  buzzer.on()
  time.sleep(1)
  buzzer.off()
  time.sleep(1)
