import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

dac=[8, 11, 7, 1, 0, 5, 12, 6]
led=[2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]


def adc():
    n = 0
    while 
    return(n)

try:
    while True:
        Vn =adc()
        if Vn!=0:
            print(Vn*3.6/256,"В")
           

finally:
    gpio.output(dac, 0)
    gpio.cleanup()