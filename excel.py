import csv 
import RTC as today

class excel_edit:
    def __init__(self,path=None,name=None):
        self.path=path
        self.name=name
    def write_excel_header(self,headers=None):
        try:
            with open(self.path+self.name+'.csv','w',newline='') as file:
                if headers == None :
                    headers=['Register1','Register2','Register3','Register4','Register5',\
                        'Register6','Register7','Register8','Register9','Register10']
                csv_writer = csv.DictWriter(file, headers)
                csv_writer.writeheader()
                print('File Generated. ')
        except:
            print('File Error. ')
    def write_excel(self,data=None,headers=None):
        try:
            with open(self.path+self.name+'.csv','w',newline='') as file:
                if headers == None :
                    headers=['Register1','Register2','Register3','Register4','Register5',\
                        'Register6','Register7','Register8','Register9','Register10']
                csv_writer = csv.DictWriter(file, headers)
                csv_writer.writeheader()
                csv_writer.writerow(dict(zip(headers,data)))
                print('File Generated. ')
        except:
            print('File Error. ')

    def append_excel(self,data,headers=None):
        try:
            with open(self.path+self.name+'.csv','a',newline='') as file:
                    csv_writer = csv.DictWriter(file, headers)
                    csv_writer.writerow(dict(zip(headers,data)))
               
        except:
            print('File Error. ')
            try:
                write_excel()
            except:
                print('File Error. ')


    def read_excel(self):
        with open(self.path+self.name+'.csv','r',newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
            
if __name__ == "__main__":
    print(today.RTC().date())    
    ex_data=[today.RTC().date(),str(today.RTC().hour)+':'+str(today.RTC().minute),123,456,123,456,123,45,123,456,123,456]
    print(len(ex_data))
    ex_headers=['Date','Time','Do','D1','D2','D3','D4','D5','D6','D7','D8','D9']
    print(len(ex_headers))
    # filename = "{}{} {}-{} .csv".format("name",str(today.RTC().date()),str(today.RTC().hour),str(today.RTC().minute))
    # jalvis=excel_edit(input('Enter file path: '),filename)
    jalvis=excel_edit(input('Enter file path: '),input('Enter file name: '))
    # jalvis.write_excel(ex_data,ex_headers)
    for i in range(1):
        jalvis.append_excel(ex_data,ex_headers) 
