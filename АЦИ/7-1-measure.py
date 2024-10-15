import RPi.GPIO as gpio
from matplotlib import pyplot
import time

gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
led=[2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(led, gpio.OUT)
gpio.setup(troyka, gpio.OUT)
gpio.output(troyka, 1) 
gpio.setup(comp, gpio.IN)

def dec2bin(n): #Перевод десятичной в двоичную запись числа
    return[int (element) for element in bin(n)[2:].zfill(8)]
def adc(): #Функция по определению напряжения с помощью модуля COMP
    DACout= [1,0,0,0, 0,0,0,0]
    gpio.output(dac, DACout)
    for i in range(8):
        time.sleep(0.005)  
        if gpio.input(comp) ==1:
            DACout[i] = 0 
        if i!=7:
            DACout[i+1] = 1  
        gpio.output(dac, DACout) 
        time.sleep(0.005)       
    return(DACout)  
def bin2dec(n): ##Перевод двоичную в десятичную запись числа
    num =0
    s = 7
    for i in range(8):
        num+= n[i]*2**s
        s-=1
    return(num)
try:
    resultat_ismer=[]
    voltage =0
    t0=time.time()
    count =0
    print("начало зарядки конденсатора")
    while voltage < 100:
        voltage = bin2dec(adc()) #число от 0 до 255
        resultat_ismer.append(voltage)
        gpio.output(led, adc())
        time.sleep(0.01)
        count+=1

    print("начало разрядки конденсатора")
    gpio.output(troyka, 0)   

    while voltage >50:
        voltage = bin2dec(adc())
        resultat_ismer.append(voltage)
        gpio.output(led, adc())
        time.sleep(0.01)
        count+=1

    time_experiment = time.time() - t0  
    
    print(resultat_ismer)   

    #запись данных в файлы
    print('запись данных в файл')
    with open('/home/b03-402/Desktop/KuznetsovNV/getLAB/АЦИ/data.txt', 'w') as f:
        for i in resultat_ismer:
            f.write(str(i) + '\n')
    with open('/home/b03-402/Desktop/KuznetsovNV/getLAB/АЦИ/settings.txt', 'w') as f:
        f.write(str(count/time_experiment) + " средняя частота дискретизации"+ "\n")
        f.write(str(3.3/256) + " шаг квантования АЦП")
        
    
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, count/time_experiment, 0.013))

    #графики
    print('построение графиков')
    y=[i/256*3.3 for i in resultat_ismer]
    x=[i*time_experiment/count for i in range(len(resultat_ismer))]
    pyplot.plot(x, y)
    pyplot.xlabel('время')
    pyplot.ylabel('вольтаж')
    pyplot.show()  

finally:
    gpio.output(dac, 0)
    gpio.output(led, 0)
    gpio.cleanup()