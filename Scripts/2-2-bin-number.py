import RPi.GPIO as GPIO
import time



dac = [26, 19, 13, 6, 5, 11 ,9, 10]
null = [0, 0, 0, 0, 0, 0 ,0 ,0]

#number = [0, 0, 0, 0, 0, 0, 1, 0]
#number = [1, 1, 1, 1, 1, 1, 1, 1]
#number = [0, 1, 1, 1, 1, 1, 1, 1]
number = [0, 0, 1, 0, 0, 0, 0, 0]
#number = [0, 0, 0, 1, 0, 0, 0, 0]
#number = [0, 0, 0, 0, 0, 1, 0, 1]
#number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

GPIO.output (dac, number)
time.sleep (10)

GPIO.output (dac, null)
GPIO.cleanup()