from time import sleep
from Cache import Cache
from Controller import Controller
from InstGenerator import InstructionGenerator

from Instruction import *
from Memory import Memory
from Protocol import Bus

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
                
                #print(self.ID+': '+instruction.istring()+'\n')
                self.execute_instruction(instruction)
                ind=self.BUS.search_cache(self.ID)
                self.BUS.CACHE_LIST[ind].iprint()
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

    def execute_instruction(self, instruction):
        if(instruction.OPERATION=="WRITE"):
            self.BUS.write(self.ID,instruction.ADDRESS,instruction.DATA)
            instruction.iprint()
        elif(instruction.OPERATION=="READ"):
            instruction.iprint()
            self.BUS.read(self.ID,instruction.ADDRESS)
        else:
            instruction.iprint()


    def read(self,address):
        print("READ ADDRESS "+address)
    


"""
#cpu_01=Processor("CPU@01")
#cpu_01.calc()
ID1="CPU@01"
ID2="CPU@02"
ID3="CPU@03"
ID4="CPU@04"
mem= Memory(0)
controller_list=[Controller(ID1,mem,Cache(ID1)),Controller(ID2,mem,Cache(ID2)),Controller(ID3,mem,Cache(ID3)),Controller(ID4,mem,Cache(ID4))]
print("***************#1**********************************")
mem.write('0000','0x999')
mem.write('0010','0x999')
mem.write('0100','0x999')
mem.write('1000','0x999')
#mem.iprint()
#cache_list=[Cache(ID1),Cache(ID2),Cache(ID3),Cache(ID4)]
bus= Bus(controller_list,mem)
proc=Processor(ID1,bus,0)
proc.run()
"""