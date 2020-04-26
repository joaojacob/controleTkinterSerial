import serial, configparser

config = configparser.ConfigParser()
config.read('conf.ini')

ser = serial.Serial(
        port=config['CONF']['port'],
        baudrate=int(config['CONF']['baudrate']),
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=int(config['CONF']['timeout']))

def openSerial():
    try:
        ser.open()
    except Exception as e:
        print("Exception: Opening serial port: " + str(e))


def readSerial():
    if ser.isOpen():
        while True:
            mens = ser.readline().decode("utf-8").strip('\n').strip('\r')
            if len(mens) == 0:
                break
            return(mens)
        return 'semLeitura'
    else:
        print("porta nao aberta")

def closeSerial():
    ser.close()

def writeSerial(text):
    if ser.isOpen():
        ser.write(text)