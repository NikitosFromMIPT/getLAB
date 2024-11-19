import RPi.GPIO as GPIO
from matplotlib import pyplot as plt


GPIO.setmode(GPIO.BCM)

knop_in = 24

GPIO.setup(knop_in, GPIO.IN)



def wait_for_Open():

    print("The door is close :<")

    while GPIO.input( knop_in > 0 ):
        pass

    print("The door is open!!!!!!!!!!!!")


try:
    wait_for_Open()


    #while True:
    #    volts.append( (adc()/256) * 3.3 )

except:
    print("THATS ALL FOXES")