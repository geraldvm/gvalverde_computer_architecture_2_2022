import threading

from Processor import *
from Memory import *
from Controller import *
from Protocol import *

class Multiprocessor:
    def __init__(self,id_1,id_2,id_3,id_4,timer):
        ID1=id_1
        ID2=id_2
        ID3=id_3
        ID4=id_4
        self.TIMER=timer
        self.MEMORY=Memory(self.TIMER/4)
        self.CONTROLLER_LIST=[Controller(ID1,self.MEMORY,Cache(ID1)),Controller(ID2,self.MEMORY,Cache(ID2)),Controller(ID3,self.MEMORY,Cache(ID3)),Controller(ID4,self.MEMORY,Cache(ID4))]
        self.BUS=Bus(self.CONTROLLER_LIST,self.MEMORY)
        self.cpu_01=Processor(ID1,self.BUS,self.TIMER)
        self.cpu_02=Processor(ID2,self.BUS,self.TIMER)
        self.cpu_03=Processor(ID3,self.BUS,self.TIMER)
        self.cpu_04=Processor(ID4,self.BUS,self.TIMER)
        self.MODE=0
        
    def run(self):
       
        th1= threading.Thread(name=self.cpu_01.ID, target=self.cpu_01.run,args=())
        th2= threading.Thread(name=self.cpu_02.ID, target=self.cpu_02.run,args=())
        th3= threading.Thread(name=self.cpu_03.ID, target=self.cpu_03.run,args=())
        th4= threading.Thread(name=self.cpu_04.ID, target=self.cpu_04.run,args=())
        th1.start()
        th2.start()
        th3.start()
        th4.start()
    
   

    
    def test(self):
        self.cpu_01.test()
"""
ID1="CPU@01"
ID2="CPU@02"
ID3="CPU@03"
ID4="CPU@04"
TIMER=0
mt = Multiprocessor(ID1,ID2,ID3,ID4,TIMER)
mt.run()
"""
