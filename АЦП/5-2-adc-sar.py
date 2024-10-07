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
def bin2dec(n):
    num =0
    s = 7
    for i in range(8):
        num+= n[i]*2**s
        s-=1
    return(num)

def adc():
    DACout= [1,0,0,0, 0,0,0,0]
    gpio.output(dac, DACout)
    for i in range(8):
        if comp ==1:
            DACout[i] = 0
            DACout[i+1] = 1
            gpio.output(dac, DACout) # в модуле DAC выводим ддвоичную запись числа i
            time.sleep(0.005)
        else:
            DACout[i+1] = 1
            gpio.output(dac, DACout) # в модуле DAC выводим ддвоичную запись числа i
            time.sleep(0.005)     
    return(DACout)    

try:
    while True:
        Vn = bin2dec(adc())
        if Vn!=0:
            print(Vn*3.6/256,"В")
           

finally:
    gpio.output(dac, 0)
    gpio.cleanup()