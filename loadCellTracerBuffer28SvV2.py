from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusSerialClient as serialClient
import time
import excel
import RTC
import threading
import matplotlib.pyplot as plt
import numpy as np
import os

try:
    os.chdir("c:")
    c = os.getcwd()
    neededPath = c+"Dashpot\\"+ str(RTC.RTC().date())
    if not os.path.isdir(neededPath): os.makedirs(neededPath)
except:
    print("File system error.")

filepath = neededPath+"\\"
client = serialClient(
method='ascii',
port='COM12',
baudrate=115200,
timeout=3,
parity='E',
stopbits=1,
bytesize=7 )
print("Communication on: {}".format(client))
def mainFunc():
    try:
        startTime = time.time()
        monitorTime = startTime + logFileTime
        resBuffer = []
        client.write_register(address=4096+85, value=0, unit=1)
        fltBuffer = []
        logFileTimemm = logFileTime * 1000
        TempSingleSampleTime = 0
        SingleSampleTime = 0
        while client.connect():
            currentTime = time.time()
            result = client.read_holding_registers(address=4096+10,count=3,unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, wordorder=Endian.Little)
            fltBuffer.append(decoder.decode_32bit_float())
            if currentTime >= monitorTime:
                SingleSampleTime = logFileTimemm/len(fltBuffer)
                name = input("Enter the File Name: ") 
                if name == '': name = "Reading"
                filename = "{2}-{3} {0} {1}.csv".format(name,str(RTC.RTC().date()),str(RTC.RTC().hour),str(RTC.RTC().minute))
                ex_jalvis = excel.excel_edit(filepath,filename)
                ex_headers=['Date','ms','Weight']
                ex_jalvis.write_excel_header(ex_headers)                                                      
                for o in range(len(fltBuffer)):
                    TempSingleSampleTime = SingleSampleTime + TempSingleSampleTime
                    ex_data=[RTC.RTC().date(),TempSingleSampleTime,fltBuffer[o]]
                    ex_headers=['Date','ms','Weight']
                    ex_jalvis.append_excel(ex_data,ex_headers)
                break      
        feedBack = "Log successfull."
        print("Close the graph window for next reading!\n thank you.")
        plt.figure(num="Graph", figsize=(13, 6), edgecolor='red', facecolor='grey', frameon =True)
        plt.plot([i*SingleSampleTime for i in range(len(fltBuffer))],fltBuffer)        
        plt.xlabel('Time in ms')
        plt.ylabel('Weight in g')
        plt.title('Load cell Graph')
        plt.yscale('linear')
        plt.axis([0, logFileTimemm, minWeight, maxWeight])
        # plt.yticks([yVal for yVal in range(0,maxWeight,int(maxWeight/20))],rotation=0)
        plt.grid(True)
        plt.show()
        return feedBack
    except:
        feedBack = "Log Fail. Check Plc Communication."
        return feedBack

while True:
    logAck = input("Type 'yes' and press 'Enter', if you want to generate Log: ")
    os.system('cls')
    if logAck == "yes":
        logFileTime = 0
        varTemp = 3
        while logFileTime < varTemp: 
            try:   
                logFileTime = int(input("Enter the time interval in sec to generate csv file: "))
            except:
                print("Enter Valid Input")
                logFileTime = int(input("Enter the time interval in sec to generate csv file: "))
            if logFileTime < varTemp:
                print("The min value is 3 sec")
        varTemp = 100
        maxWeight = 0
        while maxWeight < varTemp: 
            try:   
                maxWeight = int(input("Enter the max weight for the trial in grams: "))
            except:
                print("Enter Valid Input")
                maxWeight = int(input("Enter the max weight for the trial in grams: "))
            if maxWeight < varTemp:
                print("The min value is 100g")
        varTemp = -1
        minWeight = 1 + maxWeight
        while int(minWeight) > int(maxWeight): 
            try:   
                minWeight = int(input("Enter the min weight for the trial in grams: "))
            except:
                print("Enter Valid Input")
                minWeight = int(input("Enter the min weight for the trial in grams: "))
        input("Press Enter to start")
        print("Log will be generated after %d sec"% logFileTime)
        try:
            client.write_register(address=4096+86, value=0, unit=1)
            time.sleep(1)
            client.write_register(address=4096+86, value=1, unit=1)
            print (mainFunc())
        except:
            print("Log Fail. Check Plc Communication.")

    else:
        print("Thank You!")
        break



        
        