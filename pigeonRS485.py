
import time
from serial import *

print('Starting script with RS232 cummunication')

ser = Serial('/dev/ttyRS485', baudrate = 9600,
                    parity = PARITY_NONE,
                    stopbits = STOPBITS_ONE,
                    bytesize = EIGHTBITS)

time.sleep(1)

try:
    ser.write('Hello\n\r'.encode('utf-8'))
    ser.write('I am Pigeon\n\r'.encode('utf-8'))
    ser.write('Here I can send data using RS232\n\r'.encode('utf-8'))
    print('RS232 communication works correctly')

except KeyboardInterrupt:
    print('Exiting program')

finally:
    ser.close()
    pass
