
from pigeonRB import *
import time

out_val = 1
out_nr = 1
bo_values = [False, True, False, False, True, True, False, False]   # binary outputs values
bi_values = []                                                      # binary inputs values
di_values = []                                                      # dry contact inputs values
ai_values = []                                                      # analog inputs values
ao_values = [550, 800]                                              # analog outputs values
separator = "----------------------\n\r"

pigeonSetup(Model.RB300_CM3)
enableOutputs(True)
turnOffAllBinOutputs()

# initial values of outputs
writeBinOutputs(bo_values)
writeAnalogOutputs(ao_values)

while True:
    # read inputs
    readBinInputs(bi_values, di_values)
    readAnalogInputs()

    # print inputs states
    print("\033[H\033[J")   #clear terminal
    print("\033[1;1H")      #move cursor to (1,1)
    print(separator)
    print("Pigeon RB300\n\r")
    print(separator)
    print(separator)

    for i in range(0, len(di_values)):
        print("IND{} = {}".format(i + 1,di_values[i]))

    print(separator)

    for i in range(0, len(bi_values)):
        print("IN{} = {}".format(i + 1,bi_values[i]))

    print(separator)

    for i in range(0, len(readAnalogInputs())):
        print('AI{} = {}'.format(i + 1, readAnalogInputs()[i]))

    print(separator)

    time.sleep(2)
    exit(separator)
