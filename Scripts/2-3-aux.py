import RPi.GPIO as GPIO
import time

null = [0, 0, 0, 0, 0, 0 ,0 ,0]
leds = [21, 20, 16, 12, 7, 8 ,25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setmode (GPIO.BCM)
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (aux, GPIO.IN, pull_up_down = PUD_UP)

try:
    while True :
        for count in range (len(leds)):
            GPIO.output (leds[count], GPIO.input (aux[count]))
finally:
        GPIO.output (leds, null)
        GPIO.cleanup()