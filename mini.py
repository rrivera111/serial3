import minimalmodbus
from datetime import datetime
import time
import serial
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)



instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = 'N' #minimalmodbus.serial.PARITY_MARK , ttyAMA0, serial0
instrument.serial.stopbits = 1
instrument.serial.timeout =1
instrument.mode = minimalmodbus.MODE_RTU

while(1):
    try:#
        val = instrument.read_registers(0x1107,2) #0x3E8
        #val = instrument.read_registers(0x0020,1) #0x3E8
        # ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttotal voltage
        #val = instrument.read_registers(0x1106,2) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8val = instrument.read_registers(0x1107,1) #0x3E8
        # Registernumber, number of decimals
        print (val)
    except IOError:
        error_msg = "Failed to read from device"
        error_time = datetime.now()
        
        print ("IO Error Time" + str(error_time.isoformat()) +str(error_msg) )

    except ValueError:
        error_msg = "Failed to read CRC"
        error_time = datetime.now()
        print ("Value Error Time" + str(error_time.isoformat()) + str(error_msg))
    time.sleep(1)

