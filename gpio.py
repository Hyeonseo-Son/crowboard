import RPi.GPIO as GPIO
import time

pin1 = 11
pin2 = 16
pin3 = 17
pin4 = 18
pin5 = 19
pin6 = 20


def led_on(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)

def led_off(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    GPIO.cleanup(pin)

led_on(pin1)
print('led ON')
time.sleep(1)
led_off(pin1)
print('led OFF')
time.sleep(1)
led_on(pin2)
print('led ON')
time.sleep(1)
led_off(pin2)
print('led OFF')
time.sleep(1)
led_on(pin3)
print('led ON')
time.sleep(1)
led_off(pin3)
print('led OFF')
time.sleep(1)
led_on(pin4)
print('led ON')
time.sleep(1)
led_off(pin4)
print('led OFF')
time.sleep(1)
led_on(pin5)
print('led ON')
time.sleep(1)
led_off(pin5)
print('led OFF')
time.sleep(1)
led_on(pin6)
print('led ON')
time.sleep(1)
led_off(pin6)
print('led OFF')
time.sleep(1)

