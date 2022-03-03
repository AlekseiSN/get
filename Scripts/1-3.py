import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(23, GPIO.IN)
GPIO.setup(22, GPIO.IN)

GPIO.output(12, GPIO.input(23))
time.sleep (3)

GPIO.output(12, GPIO.input(22))
time.sleep (3)

GPIO.output(12, GPIO.input(23))
time.sleep (3)

GPIO.output(12, GPIO.input(22))
time.sleep (3)

GPIO.output(12, 0)