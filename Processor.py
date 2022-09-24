from time import sleep
from InstGenerator import InstructionGenerator

from Instruction import *

class Processor:
    def __init__(self,id,bus,timer):
        self.ID=id
        self.generator=InstructionGenerator(self.ID)
        self.EXCECUTION_MODE=0x200
        self.TIMER=timer
        self.BUS=bus
        #0x100 -> MANUAL
        #0x200 -> AUTOMATIC
    
    def calc(self):
        print(self.ID+": Calc()")

    def run(self):
        i=0
        while i<5:
            if(0x200==self.EXCECUTION_MODE):
                self.generator.auto_generate()
                instruction=self.generator.instruction
                instruction.iprint()
                #print(self.ID+': '+instruction.istring()+'\n')
                excecute_instruction(instruction)
                sleep(self.TIMER)
            else:
                print("MANUAL EXCECUTION MODE")
                instruction = self.generator.man_generate()
                #print(self.ID+': '+instruction.istring()+'\n')
                sleep(self.TIMER)
                #instruction=self.generator.
            i+=1

    
    def write(self,address,data):
        print("WRITE DATA "+data+" IN ADDRESS "+address)

    def excecute_instruction(self, instruction):
        if(instruction.OPERATION=="WRITE"):
            self.BUS.write(self.ID,instruction.ADDRESS,instruction.DATA)
            print(self.OPERATION+' '+self.ADDRESS+';'+self.DATA)
        elif(instruction.OPERATION=="READ"):
            print(self.OPERATION+' '+self.ADDRESS)
            self.BUS.read(self.ID,instruction.ADDRESS)
        else:
            print(instruction.OPERATION)


    def read(self,address):
        print("READ ADDRESS "+address)
    
    def test(self):
        print("SSSSS")
    


#cpu_01=Processor("CPU@01")
#cpu_01.calc()