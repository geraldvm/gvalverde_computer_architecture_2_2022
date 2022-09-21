from time import sleep
from InstGenerator import InstructionGenerator

from Instruction import *

class Processor:
    def __init__(self,id):
        self.ID=id
        self.generator=InstructionGenerator()
        self.EXCECUTION_MODE=0x200
        #0x100 -> MANUAL
        #0x200 -> AUTOMATIC
    
    def calc(self):
        print(self.ID+": Calc()")

    def run(self,timer):
        i=0
        while i<5:
            if(0x200==self.EXCECUTION_MODE):
                self.generator.auto_generate()
                instruction=self.generator.instruction
                #instruction.iprint()
                print(self.ID+': '+instruction.istring()+'\n')
                sleep(timer)
            else:
                print("MANUAL EXCECUTION MODE")
                instruction = self.generator.man_generate()
                print(self.ID+': '+instruction.istring()+'\n')
                sleep(timer)
                #instruction=self.generator.
            i+=1

    
    def write(self,address,data):
        print("WRITE DATA "+data+" IN ADDRESS "+address)

    def read(self,address):
        print("READ ADDRESS "+address)

#cpu_01=Processor("CPU@01")
#cpu_01.calc()