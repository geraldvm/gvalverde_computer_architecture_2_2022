import threading

from Processor import *

class Multiprocessor:
    def __init__(self):
        self.cpu_01=Processor("CPU@01")
        self.cpu_02=Processor("CPU@02")
        self.cpu_03=Processor("CPU@03")
        self.cpu_04=Processor("CPU@04")
    
    def run(self, timer):
       
        th1= threading.Thread(name=self.cpu_01.ID, target=self.cpu_01.run,args=(timer,))
        th2= threading.Thread(name=self.cpu_02.ID, target=self.cpu_02.run,args=(timer,))
        th3= threading.Thread(name=self.cpu_03.ID, target=self.cpu_03.run,args=(timer,))
        th4= threading.Thread(name=self.cpu_04.ID, target=self.cpu_04.run,args=(timer,))
        th1.start()
        th2.start()
        th3.start()
        th4.start()


mt = Multiprocessor()
mt.run(0)
