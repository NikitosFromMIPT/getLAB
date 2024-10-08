import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]

try:
    T = input("Введите период треугольного сигнала (Положительное число)")
    while True:
        
        if T=="q":
            sys.exit

        elif T.isdigit() == False:
            print("ВВЕДИТЕ ЧИСЛО, А НЕ ТЕКСТ")

        elif int(T) < 0:
            print("ВВЕДИТЕ ПОЛОЖИТЕЛЬНОЕ ЧИСЛО !!! ")

        else:
            t = int(T)/2/256
            for i in range(256):
                print(dec2bin(i))
                gpio.output(dac, dec2bin(i))
                print(int(i)*3.3/256, "В")
                sleep(t)
            for i in range(255,-1,-1):
                gpio.output(dac, dec2bin(i))
                print(int(i)*3.3/256, "В")
                sleep(t)

except KeyboardInterrupt:
    print('Программа была остановленна с клавиатуры')
except ValueError:
    print("ВВЕДИТЕ ЧИСЛО ПРАВИЛЬНО !!! ")

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
