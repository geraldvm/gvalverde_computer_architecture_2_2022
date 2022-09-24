import math, random
from Instruction import *
class InstructionGenerator:
    def __init__(self,processor_id):
        self.__operations= ['CALC','READ','WRITE']
        self.instruction=Instruction(processor_id)
        self.__READ_OPERATION=0
        self.__WRITE_OPERATION=1
        self.__CALC_OPERATION=2
        self.PROC_ID=processor_id
        

    def Poisson_distribution(self, x, lam=1):
        fact = math.factorial(x)
        prob = (math.pow(lam, x)* math.exp(-lam)) / fact
        return prob
   
    def __randomPoisson(self, range):

        while True:        
            ind = random.randint(0, range)
            dist = random.uniform(0.0, 1.0)        
            if dist >= self.Poisson_distribution(ind):
                return ind
    
    def __dataGenerate(self):
        hexa=hex(random.randint(0, 65535)) #16 Bits
        return hexa
    
    def auto_generate(self):
        ind=self.__randomPoisson(2)
        self.instruction.set_operation(ind)
        addr=self.__randomPoisson(7)
        if(self.instruction.OPERATION=="WRITE"):
            self.instruction.set_data(self.__dataGenerate())
            self.instruction.set_address(addr)
        if(self.instruction.OPERATION=="READ"):
            self.instruction.set_address(addr)
        return self.instruction

    def generate_calc(self):
        self.instruction.set_operation(self.__CALC_OPERATION)
        self.instruction.set_address(8)
        self.instruction.set_data(-1)
        return self.instruction

    def generate_read(self, address):
        self.instruction.set_operation(self.__READ_OPERATION)
        self.instruction.set_address_man(address)
        self.instruction.set_data(-1)
        return self.instruction
    
    def generate_write(self, address, data):
        self.instruction.set_operation(self.__WRITE_OPERATION)
        self.instruction.set_address_man(address)
        self.instruction.set_data(data)
        return self.instruction
        
#inst=InstructionGenerator()
#inst.generate()
#inst.instruction.iprint()
