from time import sleep
from InstGenerator import InstructionGenerator

from Instruction import *


class Processor:
    def __init__(self,id,bus,timer):
        self.ID=id
        self.generator=InstructionGenerator(self.ID)
        self.EXECUTION_MODE='AUTO'
        self.TIMER=timer
        self.BUS=bus
        self.INSTRUCTION=Instruction(self.ID)
        self.RUN_STATE='RUN'
        self.INPUT_INS=['','','']
        #0x100 -> MANUAL
        #0x200 -> AUTOMATIC
    
    def calc(self):
        print(self.ID+": Calc()")

    def run(self):
        i=0
        while (i<10):
            if('AUTO'==self.EXECUTION_MODE):
                if('RUN'==self.RUN_STATE):
                    
                    self.generator.auto_generate()
                    self.INSTRUCTION=self.generator.instruction
                    self.execute_instruction(self.INSTRUCTION)
                    sleep(self.TIMER)

                elif('PAUSE'==self.RUN_STATE):
                    #print("PAUSE")
                    sleep(self.TIMER/10)
                
                elif('STEP'==self.RUN_STATE):
                    self.generator.auto_generate()
                    self.INSTRUCTION=self.generator.instruction
                    self.execute_instruction(self.INSTRUCTION)
                    self.RUN_STATE='PAUSE'
                    print("STEP")
                    sleep(self.TIMER)
                
            elif('MAN'==self.EXECUTION_MODE):
                print("MANUAL EXCECUTION MODE")
                if('READ'==self.INPUT_INS[0]):
                    self.INSTRUCTION = self.generator.generate_read(self.INPUT_INS[1])
                if('WRITE'==self.INPUT_INS[0]):
                    self.INSTRUCTION = self.generator.generate_write(self.INPUT_INS[1],self.INPUT_INS[2])
                else:
                    self.INSTRUCTION = self.generator.generate_calc()
                self.execute_instruction(self.INSTRUCTION)
                sleep(self.TIMER)
                self.EXECUTION_MODE='0'
                #instruction=self.generator.
            elif('STOP'==self.EXECUTION_MODE):
                return
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