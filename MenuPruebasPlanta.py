import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC

import time
#class Prueba:
def __init__():
    while True:
        print ("Opciones: "
               "\n1: SALIDAS DIGITALES"
               "\n2: PWM"
               "\n3: Entradas Analogas")
        opt = input("Introduce una opcion")
        Menu(opt)

def Menu(opt):
    if(opt == 1):
        print("Trabajando SALIDAS DIGITALES")
        time.sleep(3)
        functionGPIO()
    elif(opt == 2):
        print("Trabajando PWM")
        time.sleep(3)
        #functionPWM()
    elif(opt == 3):
        print("Trabajando ADC")
        time.sleep(3)
        #functionPWM()


def functionGPIO():
    ports = ["P8_7", "P8_8", "P8_9", "P8_10", "P8_11", "P8_12", "P8_14", "P8_15", "P8_16", "P8_17", "P8_18"]
    for x in ports:
        print (x)
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(x, GPIO.LOW)
    print ("\nListo\n")

__init__()