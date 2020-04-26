from pySerial import *


def ligar():
    writeSerial(b'H')
    #readS = readSerial()
    #print(readS)

def desligar():
    writeSerial(b'L')
    #readS = readSerial()
    #print(readS)