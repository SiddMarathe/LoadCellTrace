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
        start = datetime.
        result = client.read_holding_registers(address=130+4096,count=70,unit=1)
        resBuffer.append(result.registers)
        result = client.read_holding_registers(address=130+70+4096,count=70,unit=1)
        resBuffer.append(result.registers)
        client.write_register(address=85+4096, value=0, unit=1)
    except:
        print(" Error ")