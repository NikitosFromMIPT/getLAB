import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]


def adc():
    for i in range(2^8):
        gpio.output(dac, dec2bin(i)) # в модуле DAC выводим ддвоичную запись числа i
        time.sleep(0.01)
        if gpio.input(comp) == 1: # пин COMP выход компаратора, если он считывает 0 то cигнал на DAC больше сигнала на тройке модуле
            return(i)

try:
    while True:
        Vn =adc()
        if Vn!=None:
            print(Vn)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()