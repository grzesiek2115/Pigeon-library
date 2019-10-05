from pigeonRB import *
import time

enableOutputs(True)
pigeonSetup(Model.RB300)

while True:
    in1 = 1 - readDryInput(1)
    in2 = 1 - readDryInput(2)

    out5 = in1
    out6 = in1 | in2    #bitwise OR
    out7 = in1 & in2    #bitwise AND
    out8 = in1 ^ in2    #bitwise XOR

    writeBinOutput(5, out5)
    writeBinOutput(6, out6)
    writeBinOutput(7, out7)
    writeBinOutput(8, out8)


