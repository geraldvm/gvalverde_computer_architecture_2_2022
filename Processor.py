from time import sleep
from InstGenerator import InstructionGenerator

from Instruction import *

class Processor:
    def __init__(self,id):
        self.ID=id
        self.generator=InstructionGenerator()
    
    def calc(self):
        print(self.ID+": Calc()")

    def run(self,timer):
        i=0
        while i<5:
            
            self.generator.generate()
            instruction=self.generator.instruction
            #instruction.iprint()
            print(self.ID+': '+instruction.istring()+'\n')
            sleep(timer)
            i+=1

    
    def write(self,address,data):
        print("WRITE DATA "+data+" IN ADDRESS "+address)

    def read(self,address):
        print("READ ADDRESS "+address)

#cpu_01=Processor("CPU@01")
#cpu_01.calc()