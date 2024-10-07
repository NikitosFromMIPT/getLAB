import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
pinPWM= 13                       # указать пин, который будет задавать ШИМ
gpio.setup(pinPWM, gpio.OUT)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]
T=1/1000
try:
    while True:
        D = input("Введите коэффицент заполнения (Положительное число о 0 до 100)")
        if D=="q":
            sys.exit

        elif D.isdigit() == False:
            print("ВВЕДИТЕ ЧИСЛО, А НЕ ТЕКСТ")

        elif int(D) < 0:
            print("ВВЕДИТЕ ПОЛОЖИТЕЛЬНОЕ ЧИСЛО !!! ")

        else:
            t = T*D/100
            gpio.output(pinPWM, 1)
            print(3.3, "В")
            sleep(t)
            gpio.output(pinPWM, 0)
            print(0.0, "В")
            sleep(T-t)


except KeyboardInterrupt:
    print('Программа была остановленна с клавиатуры')
except ValueError:
    print("ВВЕДИТЕ ЧИСЛО ПРАВИЛЬНО !!! ")

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
