import spidev
import math
import time

def spiClose():
    spi = spidev.SpiDev()  # create spi object
    spi.open(0, 1)  # open spi port 0, device (CS) 1
    spi.mode = 1  # mode bits: CPHA = 1, CPOL = 0,
    spi.bits_per_word = 8
    spi.max_speed_hz = 2000000
    spi.close()


def spiWriteAO(val):
    spi = spidev.SpiDev()  # create spi object
    spi.open(0, 1)  # open spi port 0, device (CS) 1
    spi.mode = 1  # mode bits: CPHA = 1, CPOL = 0,
    spi.bits_per_word = 8
    spi.max_speed_hz = 2000000
    a = (val[0] % 256)
    b = (val[0] / 256)
    c = (val[1] % 256)
    d = (val[1] / 256)
    bb = math.floor(b)
    dd = math.floor(d)
    spi.writebytes([0x4F, a, bb, c, dd])


def spiReadAI():
    spi = spidev.SpiDev()  # create spi object
    spi.open(0, 1)  # open spi port 0, device (CS) 1
    spi.mode = 1
    spi.bits_per_word = 8
    spi.max_speed_hz = 2000000

    spi.writebytes([0x41])
    time.sleep(0.0001)
    q = spi.readbytes(8)

    x = []

    x.append((q[0]) | (q[1] << 8))
    x.append((q[2]) | (q[3] << 8))
    x.append((q[4]) | (q[5] << 8))
    x.append((q[6]) | (q[7] << 8))

    ai_values = []

    ai_values.append(round(((x[0] * 10.065) / 1023.0), 2))
    ai_values.append(round(((x[1] * 10.065) / 1023.0), 2))
    ai_values.append(round(((x[2] * 10.065) / 1023.0), 2))
    ai_values.append(round(((x[3] * 10.065) / 1023.0), 2))

    return ai_values


