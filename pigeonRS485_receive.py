
import time
from serial import *

print('Starting script with RS485 cummunication')

ser = Serial('/dev/ttyRS485', baudrate = 9600,
                    parity = PARITY_NONE,
                    stopbits = STOPBITS_ONE,
                    bytesize = EIGHTBITS)

time.sleep(1)

while True:
    try:
        if ser.inWaiting() > 0:
            data = ser.read(size = 10)  # size is a size of reading value
            print(data.decode('utf-8'))
    except KeyboardInterrupt:
        print('Exiting program, serial port closed')
        ser.close()

    finally:
        pass
