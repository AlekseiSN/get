import RPi.GPIO as GPIO
import time

buf = [0, 0, 0, 0, 0, 0 ,0 ,0]
null = [0, 0, 0, 0, 0, 0 ,0 ,0]
dac = [26, 19, 13, 6, 5, 11 ,9, 10]
comp = 4 
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int (num) for num in bin(value)[2:].zfill(8)]

def adc():
    for value in range(255):
        time.sleep (0.001)
        GPIO.output(dac, decimal2binary(value)) 
        if GPIO.input(comp) == 0:
            return value
    return 0

    
try:
    while 1:
        v = adc() / 256 * 3.3       
        print ('v = {:3f}'.format(v))

finally:
        GPIO.output (dac, null)
        GPIO.output(troyka, 0)
        GPIO.cleanup()

