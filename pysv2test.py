from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusSerialClient as serialClient
import datetime
client = serialClient(
method='ascii',
port='COM12',
baudrate=115200,
timeout=3,
parity='E',
stopbits=1,
bytesize=7 )
print("Communication on: {}".format(client))
print(client.connect())
while client.connect():
    resNum = int(input('Enter res number: '))
    try:
        result = client.read_holding_registers(address=resNum,count=100,unit=1)
        print(result.registers)

    except:
        print(" Error ")