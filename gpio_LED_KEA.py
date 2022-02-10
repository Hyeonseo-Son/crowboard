import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
channel = 1

GPIO.setup(channel, GPIO.OUT)

while True:
   GPIO.output(channel, GPIO.HIGH)
   
   time.sleep(0.5)
   GPIO.output(channel, GPIO.LOW)

   time.sleep(0.5)

GPIO.cleanup()
