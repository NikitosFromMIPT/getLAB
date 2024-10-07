import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]

try:
    while True:
        T = input("Введите период треугольного сигнала (Положительное число)")
        if T=="q":
            sys.exit

        elif T.isdigit() == False:
            print("ВВЕДИТЕ ЧИСЛО, А НЕ ТЕКСТ")

        elif int(T) < 0:
            print("ВВЕДИТЕ ПОЛОЖИТЕЛЬНОЕ ЧИСЛО !!! ")

        else:
            t = T/2/256
            for i in range(256):
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
