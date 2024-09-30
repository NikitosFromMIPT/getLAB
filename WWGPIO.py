import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
led=[2, 3, 4, 17, 27, 22, 10, 9]
gpio.setup(dac, gpio.OUT)


def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]

print(dec2bin(10))