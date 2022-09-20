
from Processor import *
import threading

class Multiprocessor:
    def __init__(self):
        self.cpu_01=Processor("CPU@01")
        self.cpu_02=Processor("CPU@02")
        self.cpu_03=Processor("CPU@03")
        self.cpu_04=Processor("CPU@04")
    
    def run(self):
        th1= threading.Thread(name='CPU@01', target=self.cpu_01.calc())
        th2= threading.Thread(name='CPU@02', target=self.cpu_02.calc())
        th3= threading.Thread(name='CPU@03', target=self.cpu_03.calc())
        th4= threading.Thread(name='CPU@04', target=self.cpu_04.calc())
        th1.start()
        th2.start()
        th3.start()
        th4.start()

mt = Multiprocessor()
mt.run()
