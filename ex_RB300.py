

from pigeonRB import *
import time


out_val = 1
out_nr = 1
bo_values = [False, True, False, False, True, True, False, False]   #binary outputs values
bi_values = []                                                      #binary inputs values
di_values = []                                                      #dry contact inputs values
ai_values = []                                                      #analog inputs values
ao_values = [550, 1000]                                             #analog outputs values
firm = [1,2,3,4]                                                    #firmware version
separator = "----------------------\n\r"

pigeonSetup(Model.RB300_CM3)
enableOutputs(True)
#readFirmwareVer(firm)
turnOffAllBinOutputs()

#initial values of outputs
#writeBinOutputs(bo_values)
#writeAnalogOutputs(ao_values)

while True:
    #read inputs
    readBinInputs(bi_values, di_values)

    #readAnalogInputs(ai_values)

    #print inputs states
    print("\033[H\033[J")   #clear terminal
    print("\033[1;1H")      #move cursor to (1,1)
    print(separator)
    print("Pigeon RB300\n\r")
    #print("Firm ver.: {}{}{}{}".format(firm[3],firm[2],firm[1],firm[0]))
    print(separator)
    print(separator)

    for i in range(0, len(di_values)):
        print("IND{} = {}".format(i + 1,di_values[i]))

    print(separator)

    for i in range(0, len(bi_values)):
        print("IN{} = {}".format(i + 1,bi_values[i]))


    #for (index, i) in enumerate(ai_values):
    #    print("IN{} = {}".format(index + 1, ai_values[i + 1]))
    #print(separator)

    #write outputs
    writeBinOutputs(bo_values)
    #writeAnalogOutputs(ao_values)

    #calculate next values of outputs exit()



    time.sleep(2)
    exit("koniec programu")
#pigeonClose(Model.RB300_CM3)


