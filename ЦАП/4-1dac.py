import RPi.GPIO as gpio
import sys
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]



try:
    while True:
        n = input("Введите целое число от 0 до 255 ")
        if n=="q":
            sys.exit

        elif n.isdigit() == False:
            print("ВВЕДИТЕ ЧИСЛО, А НЕ ТЕКСТ")

        elif 255 < int(n) < 0 or int(n)%1!=0:
            print("ВВЕДИТЕ ЧИСЛО ПРАВИЛЬНО !!! ")

        else:
            print(int(n)*3.3/256, "В")
            print(dec2bin(int(n)))
            gpio.output(dac, dec2bin(int(n)))

except KeyboardInterrupt:
    print('Программа была остановленна с клавиатуры')
except ValueError:
    print("ВВЕДИТЕ ЧИСЛО ПРАВИЛЬНО !!! ")

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
