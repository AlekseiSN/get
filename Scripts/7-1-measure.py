import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


null = [0, 0, 0, 0, 0, 0 ,0 ,0]
tmp = [0, 0, 0, 0, 0, 0 ,0 ,0]

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11 ,9, 10]
comp = 4 
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
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

dec = 0
value = []

try:
    start_time = time.time()
    GPIO.output (troyka, 1)

    while (dec < 3.1):
        dec = adc ()
        value.append (dec)
        print ("{:.2}".format(dec))

    GPIO.output (troyka, 0)

    while (dec > 0.1):
        dec = adc ()
        value.append (dec)
        print ("{:.2}".format(dec))

    stop_time = time.time()     
    time_1 = stop_time - start_time

    print ('продолжительность эксперимента: ', time_1)
    print ('период измерения: ', time_1 / len(value))
    print ('частота дискретизации: ', len(value) / time_1)
    print ('шаг квантования: ', (3.3 / 256))

    plt.plot (value)
    plt.show()

    measured_data_str = [str(item) for item in value]

    with open("measured_data.txt", "w") as f:
        f.write ("\n".join(measured_data_str))

    with open("settings.txt", "w") as f_s:
        f_s.write ("частота дискретизации: {:.3}".format(len(value) / time_1))
        f_s.write ("шаг квантования: {:.3}".format(3.3 / 256))


finally:
        GPIO.output (dac, null)
        GPIO.output(troyka, 0)
        GPIO.cleanup()