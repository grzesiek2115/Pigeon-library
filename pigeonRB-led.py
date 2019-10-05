from pigeonRB import *
import time
pigeonSetup(Model.RB300)

while True:
    GPIO.output(LED1, False)
    time.sleep(1)
    GPIO.output(LED1, True)
    time.sleep(1)
