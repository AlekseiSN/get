import RPi.GPIO as GPIO
import time


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
    buf = [0, 0, 0, 0, 0, 0 ,0 ,0]
    for count in range(8):

        buf[count] = 1
        GPIO.output(dac, buf) 
        time.sleep(0.01)  

        if GPIO.input(comp) == 0:
            buf[count] = 0

    return (3.3)*((1/2)*buf[0] + (1/4)*buf[1] + (1/8)*buf[2] + (1/16)*buf[3] + (1/32)*buf[4] + (1/64)*buf[5] + (1/128)*buf[6] + (1/256)*buf[7])


try:
    while 1:
        v = adc()            
        print ('v = {:3f}'.format(v))


finally:
        GPIO.output (dac, null)
        GPIO.output(troyka, 0)
        GPIO.cleanup()