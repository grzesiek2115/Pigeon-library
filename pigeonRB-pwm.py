from pigeonRB import *

pigeonSetup(Model.RB300)
enableOutputs(True)

out7 = GPIO.PWM(OUT7, 50)  # GPIO.PWM(channel, frequency)
wypelnienie = 0
out7.start(wypelnienie)  # start(wypełnienie 0 - 100)

try:
    while True:
        wypelnienie += 5
        if  wypelnienie >= 100:
            wypelnienie = 0
        out7.ChangeDutyCycle(wypelnienie)  # ustawienie nowej wartości wypełnienia

except KeyboardInterrupt:
    print("Koniec")

out7.stop()
GPIO.cleanup
