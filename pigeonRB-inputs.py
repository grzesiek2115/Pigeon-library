from pigeonRB import *

pigeonSetup(Model.RB300)

print("Optoisolated inputs: \n\r")
print("IN1 = {}".format(1 - readOptoInput(1)))
print("IN1 = {}".format(1 - readOptoInput(2)))
print("IN1 = {}".format(1 - readOptoInput(3)))
print("IN1 = {}".format(1 - readOptoInput(4)))
print("IN1 = {}".format(1 - readOptoInput(5)))
print("IN1 = {}".format(1 - readOptoInput(6)))
print("IN1 = {}".format(1 - readOptoInput(7)))
print("IN1 = {}".format(1 - readOptoInput(8)))
print("----------------------\n\r")
print("Dryisolated inputs: \n\r")
print("IND1 = {}".format(1 - readDryInput(1)))
print("IND2 = {}".format(1 - readDryInput(2)))
print("IND3 = {}".format(1 - readDryInput(3)))
print("IND4 = {}".format(1 - readDryInput(4)))

exit()
