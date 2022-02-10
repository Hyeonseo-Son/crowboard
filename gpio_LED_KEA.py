import Jetson.GPIO as GPIO
import time

pin1 = 1
pin2 = 7
pin3 = 9

def led_on(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)

def led_off(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.cleanup(pin)

led_on(pin1)
print('pin1 ON')
time.sleep(0.5)
led_off(pin1)
print('pin1 OFF')
time.sleep(0.5)

led_on(pin2)
print('pin2 ON')
time.sleep(0.5)
led_off(pin2)
print('pin2 OFF')
time.sleep(0.5)

led_on(pin3)
print('pin3 ON')
time.sleep(0.5)
led_off(pin3)
print('pin3 OFF')
time.sleep(0.5)
