import matplotlib.pyplot as plt
import csv
import numpy as np

class DataHouse:
    def __init__(self, time, house1, house2, house3, house4, house5):
        self.time = time
        self.house1 = house1
        self.house2 = house2
        self.house3 = house3
        self.house4 = house4
        self.house5 = house5

class DataPV:
    def __init__(self,timePV,PV):
        self.timePV=timePV
        self.PV=PV
        
class DataMubes:
    def __init__(self, timeMu, Con00, Con01, Con02):
        self.timeMu = timeMu
        self.Con00 = Con00
        self.Con01 = Con01
        self.Con02 = Con02
   
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w

def readDataHouse():
    
    pDir='/Users/mmmap/Documents/KTH/Smart_Cities/emulating/StROBe/Simulations/P.txt'
    file = open(pDir, 'r') 
    lines = file.readlines()[3:]
    file.close()
    time=[]
    house1=[]
    house2=[]
    house3=[]
    house4=[]
    house5=[]
 
    for t in lines:
    
        aux=t.split(" ")
    
        time.append(float(aux[0])/3600) #converting the data to hours
        house1.append(float(aux[1]))
        house2.append(float(aux[2]))
        house3.append(float(aux[3]))
        house4.append(float(aux[4]))
        house5.append(float(aux[5]))

    Data1=DataHouse(time, house1,house2,house3,house4,house5)
  
    return Data1

def readDataMubes():
    
    pDir='C:/Users/mmmap/Documents/KTH/Smart_Cities/Project/Runout.csv'
    file = open(pDir)
    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    time=[]
    Con00=[]
    Con01=[]
    Con02=[]
    
    rows = []
    for row in csvreader:
        time.append(row[0])
        Con00.append(float(row[2]))
        Con01.append(float(row[5]))
        Con02.append(float(row[8]))

  
    Data_Mubes=DataMubes(time,Con00,Con01,Con02) 
  
    return Data_Mubes  


def readDataPV():
    pDir='C:/Users/mmmap/Documents/KTH/Smart_Cities/Project/PV_Prod.csv'
    file = open(pDir)
    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    time=[]
    prod=[]
    
    rows = []
    for row in csvreader:
        time.append(float(row[0]))
        prod.append(float(row[1]))
  
    DataP=DataPV(time,prod) 
  
    return DataP  

def means(y): ##used to put the data hourly
    i=0
    a=[]
    for x in range(0, len(y), 60):   
        a.append(sum(y[i-59:i])/60)
        i=i+60
    
    return a

def plot(x,y,xPV,yPV):  #1440=60*24 the data is in minutes so multiply for number of hours in a day

    print(y)
    ##plt.plot(xPV, y, 'b')
    plt.plot(xPV, yPV, 'r')
  
    plt.show() 

        
def main():
    

    data=readDataHouse()
    dataPV=readDataPV()
    dataMubes=readDataMubes()

    aux=np.add(dataMubes.Con00, dataMubes.Con01)
    TotalCon=np.add(aux,dataMubes.Con02)

   
    y1=means(data.house1[0:1440])
    plot(data.time[0:1440],y1,dataPV.timePV[0:],dataPV.PV[0:])
  
    ##plot(data.time[0:24],TotalCon[0:24],dataPV.timePV[0:24],dataPV.PV[0:24])




    

if __name__ == "__main__":
    main()
