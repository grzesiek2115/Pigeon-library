from pigeonRB import *
import time
bo_values = [True, True, False, False, True, True, False, False]
enableOutputs(True)
pigeonSetup(Model.RB300)
writeBinOutputs(bo_values)
bi_values = []                                                      #binary inputs values
di_values = []

print(readOptoInput(1))

