
import time
from serial import *

print('Starting script with RS485 cummunication')

ser = Serial('/dev/ttyRS485', baudrate = 9600,
                    parity = PARITY_NONE,
                    stopbits = STOPBITS_ONE,
                    bytesize = EIGHTBITS)

ser.write('Hello\n\r'.encode('utf-8'))
ser.write('I am Pigeon\n\r'.encode('utf-8'))
ser.write('Here I can send data using RS485\n\r'.encode('utf-8'))
print('RS485 communication works correctly')

time.sleep(1)
while True:
    try:
        a = input("Send random data: ")
        ser.write(a.encode('utf-8'))

    except KeyboardInterrupt:
        print('Exiting program, serial port closed')
        ser.close()

    finally:
        pass
