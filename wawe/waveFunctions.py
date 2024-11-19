import time
from time import sleep
import RPi.GPIO as GPIO
from matplotlib import pyplot as plt


GPIO.setmode(GPIO.BCM)

comp = 4
knop_in = 24

dac=[26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(knop_in, GPIO.IN)




def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, perev(k))
        sleep(0.005)
        if GPIO.input(comp)==0:
            k-=2**i
    return k

def wait_for_Open():

    while True:
        if GPIO.input(knop_in) > 0:
            print("The door is open!!!!!!!!!!!!") 

        else:
            print("The door is close :<")


volt=[]
time_start=0
time_len=0


try:
    wait_for_Open()
    time_start=time.time() 


    while True:
        volt.append( (adc()/256) * 3.3 )

except:
    print(volt)
