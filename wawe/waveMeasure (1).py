import RPi.GPIO as GPIO
import sys
from time import sleep
import time
from matplotlib import pyplot

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
Gateway = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(Gateway, GPIO.IN)
GPIO.setup(dac, GPIO.OUT)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, perev(k))
        sleep(0.001)
        if GPIO.input(comp)==1:
            k-=2**i
    return k


def waitForOpen():                          #функция для проверки состояния двери

    if GPIO.input(Gateway) == 0:
        print('The door is open')             #если через датчик идет напряжение,
        return  True                       #то значение на Gateway
    else:
        print('The door is close')                                   #не равно 0 => дверь открыта
        return False

volt=[]
time_start=0
time_len=0

try:
    metka=0

    while metka==0:

        if waitForOpen():

            metka=1


                          #Если дверь открыта измерения и программа начинают работу
    time_start = time.time()                #Записываем время старта

    while time_len < 10:                    #Проверяем время выполнения программы

        volt.append(adc())      #смотри код с АЦП
        time_len = time.time() - time_start #Вычисляем время длительности программы

    print("ВАШИ ВЫЧИСЛЕНИЯ ЗАКОНЧИЛИСЬ. ИДЕТ ОБРАБОТКА. ПОЖАЛУЙСТА ПОДОЖДИТЕ ...") #отправляет нас в except


finally:
    with open('Волна.txt', 'w') as file:    #Создаем файл на запись
        for i in volt:                      #
            file.write(str(i) +'\n')        #записываем значения напряжения в файл
        GPIO.cleanup()                          #отчищаем малинку