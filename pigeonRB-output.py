from pigeonRB import *
import time

pigeonSetup(Model.RB300)
enableOutputs(True)

while True:
    writeBinOutput(6, True)
    time.sleep(1)
    writeBinOutput(6, False)
    time.sleep(1)
