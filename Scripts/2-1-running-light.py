import RPi.GPIO as GPIO
import time



leds = [24, 25, 8, 7, 12, 16 ,20, 21]

GPIO.setmode (GPIO.BCM)

GPIO.setup (leds, GPIO.OUT)

for count in range (3) :
    for port in leds :
        GPIO.output (port, 1)
        time.sleep (0.2)
        GPIO.output (port, 0)

GPIO.output (leds, 0)

GPIO.cleanup()



