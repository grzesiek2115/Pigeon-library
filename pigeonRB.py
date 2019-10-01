#!/usr/bin/python

import RPi.GPIO as GPIO
from enum import Enum


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Digital inputs
IN1 = 12
IN2 = 13
IN3 = 18
IN4 = 19
IN5 = 20
IN6 = 21
IN7 = 22
IN8 = 23
#Dry contact inputs
IND1 = 30
IND2 = 31
IND3 = 32
IND4 = 33
#Digital outputs
OUTE = 34
OUT1 = 35
OUT2 = 36
OUT3 = 37
OUT4 = 38
OUT5 = 39
OUT6 = 40
OUT7 = 41
OUT8 = 42
#LEDs
LED0 = 45
LED1 = 47
#Watchdog
WATCHDOG_EN = 5
WATCHDOG_IN = 44
#Power_control
CTRL_3V3 = 28
CTRL_5V = 29
FAULT_5V = 43
#LAN9514
LAN_RESET = 6
#Pigeon model type
class Model(Enum):
    UNKNOWN = 1
    RB100 = 2
    RB100_CM3 = 3
    RB300 = 4
    RB300_CM3 = 5

#Digital inputs
digitalinputs_list = [IN1, IN2, IN3, IN4, IN5, IN6, IN7, IN8]
#Dry contact inputs
digitalDryinputs_list = [IND1, IND2, IND3, IND4]
#Digital outputs
digitaloutputs_list = [OUT1, OUT2, OUT3, OUT4, OUT5, OUT6, OUT7, OUT8]

#model = "Unknown" #print(RPi.GPIO.RPI_INFO["TYPE"])

def enableOutputs(x):
    GPIO.setup(OUTE, GPIO.OUT)
    #Enable of outputs
    if x == True:
        GPIO.output(OUTE, False)  #podanie 0 na GPIO34 - umożliwienie obsuługi wyjść
    else:
        GPIO.output(OUTE, True)   #podanie 1 na GPIO34 - uniemożliwienie obsługi wyjść

def pigeonSetup(model):
    #sprawdzenie numeracji pinow - -odpowiednik wiringPiSetupGpio
    #Broadcom chip-specific pin numbers. These pin numbers follow the lower-level numbering system defined by the Raspberry Pi's Broadcom-chip brain.
    if GPIO.BCM == 11:  #print(GPIO.BCM)
        pass
    else:
        exit("ERROR: Wrong Pin Numbering Declaration.")


    #Digital outputs - ustawione
    GPIO.setup(OUT1, GPIO.OUT)
    GPIO.setup(OUT2, GPIO.OUT)
    GPIO.setup(OUT3, GPIO.OUT)
    GPIO.setup(OUT4, GPIO.OUT)
    GPIO.setup(OUT5, GPIO.OUT)
    GPIO.setup(OUT6, GPIO.OUT)
    GPIO.setup(OUT7, GPIO.OUT)
    GPIO.setup(OUT8, GPIO.OUT)
    # Enable all outputs
    enableOutputs(True)
    #Digital optoisolated inputs - ustawienie
    GPIO.setup(IN1, GPIO.IN)
    GPIO.setup(IN2, GPIO.IN)
    GPIO.setup(IN3, GPIO.IN)
    GPIO.setup(IN4, GPIO.IN)
    GPIO.setup(IN5, GPIO.IN)
    GPIO.setup(IN6, GPIO.IN)
    GPIO.setup(IN7, GPIO.IN)
    GPIO.setup(IN8, GPIO.IN)
    #Dry contact inputs
    GPIO.setup(IND1, GPIO.IN)
    GPIO.setup(IND2, GPIO.IN)
    GPIO.setup(IND3, GPIO.IN)
    GPIO.setup(IND4, GPIO.IN)
    #watchdog
    GPIO.setup(WATCHDOG_EN, GPIO.OUT)
    GPIO.setup(WATCHDOG_IN, GPIO.OUT)
    #powercontrol
    GPIO.setup(CTRL_3V3, GPIO.OUT)
    GPIO.setup(CTRL_5V, GPIO.OUT)
    GPIO.setup(FAULT_5V, GPIO.OUT)
    #LAN9514
    GPIO.setup(LAN_RESET, GPIO.OUT)
    #LED
    GPIO.setup(LED0, GPIO.OUT)
    GPIO.setup(LED1, GPIO.OUT)

    if model == Model.RB100 or model == Model.RB100_CM3:
        print("100tki") #do poprawki
    elif model == Model.RB300 or model == Model.RB300_CM3:
        print("3setki") #do poprawki
    else:
        exit("wrong model definition\n")

def pigeonClose(model):
    if model == Model.RB100 or model == Model.RB100_CM3:
        print("100tki") #do poprawki
    elif model == Model.RB300 or model == Model.RB300_CM3:
        print("3setki") #do poprawki
    else:
        exit("wrong model definition\n")


def readOptoInput(input_nr):    #Funkcja działa poprawnie
    return bool(GPIO.input(digitalinputs_list[input_nr - 1]))


def readDryInput(input_nr):     #Funkcja działa poprawnie
    return bool(GPIO.input(digitalDryinputs_list[input_nr - 1]))

def readBinInputs_insert(bi, di):      #DO SPRAWDZENIA czy działa poprawnie
    for i in range(8):
        bi.insert(i, readOptoInput(i + 1))
    for j in range(4):
        di.insert(j, readDryInput(j + 1))

def readBinInputs_append(bi, di):      #DO SPRAWDZENIA czy działa poprawnie
    for i in range(8):
        bi.append(readOptoInput(i + 1))
    for j in range(4):
        di.append(readDryInput(j + 1))

def writeBinOutput(output_nr, bool_value):   #Funkcja działa poprawnie
    GPIO.output(digitaloutputs_list[output_nr - 1], bool_value)


def writeBinOutputs(values):    #Funkcja działa poprawnie
    for i in range(8):
        GPIO.output(digitaloutputs_list[i], values[i])

def turnOffAllBinOutputs(): #Funkcja działa poprawnie
    for i in range(8):
        GPIO.output(digitaloutputs_list[i], False)


def readAnalogInputs(x):
    print("first pigeonSPI must be done")


def writeAnalogOutputs(x):
    print("first pigeonSPI must be done")


def readFirmwareVer(x):
    print("first pigeonSPI must be done")








