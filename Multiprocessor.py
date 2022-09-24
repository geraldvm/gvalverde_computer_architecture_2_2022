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
        self.cpu_01=Processor(ID1)
        self.cpu_02=Processor(ID2)
        self.cpu_03=Processor(ID3)
        self.cpu_04=Processor(ID4)
        self.MEMORY=Memory(self.TIMER/4)
        self.CONTROLLER_LIST=[Controller(ID1,self.MEMORY,Cache(ID1)),Controller(ID2,self.MEMORY,Cache(ID2)),Controller(ID3,self.MEMORY,Cache(ID3)),Controller(ID4,self.MEMORY,Cache(ID4))]
        self.BUS=Bus(self.CONTROLLER_LIST,self.MEMORY)
        self.MODE=0
        
    def run(self):
       
        th1= threading.Thread(name=self.cpu_01.ID, target=self.cpu_01.run,args=(self.TIMER,))
        th2= threading.Thread(name=self.cpu_02.ID, target=self.cpu_02.run,args=(self.TIMER,))
        th3= threading.Thread(name=self.cpu_03.ID, target=self.cpu_03.run,args=(self.TIMER,))
        th4= threading.Thread(name=self.cpu_04.ID, target=self.cpu_04.run,args=(self.TIMER,))
        th1.start()
        th2.start()
        th3.start()
        th4.start()
    
    def test(self):
        self.cpu_01.test()

ID1="CPU@01"
ID2="CPU@02"
ID3="CPU@03"
ID4="CPU@04"
TIMER=0
mt = Multiprocessor(ID1,ID2,ID3,ID4,TIMER)
mt.run()
mt.test()


mem= Memory(0)
controller_list=[Controller(ID1,self.MEMORY,Cache(ID1)),Controller(ID2,self.MEMORY,Cache(ID2)),Controller(ID3,self.MEMORY,Cache(ID3)),Controller(ID4,self.MEMORY,Cache(ID4))]
print("***************#1**********************************")
mem.write('0000',0x999)
mem.write('0010',0x560)
mem.write('0100',0x382)
mem.write('1000',0x258)
#mem.iprint()
#cache_list=[Cache(ID1),Cache(ID2),Cache(ID3),Cache(ID4)]
bus= Bus(controller_list,mem)
#bus.read(ID1,'0000')
bus.write(ID1,'0000',0x111)
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()