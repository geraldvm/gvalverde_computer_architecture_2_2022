import time, math, random, threading
from Instruction import *
class InstructionGenerator:
    def __init__(self):
        self.__operations= ['CALC','READ','WRITE']
        self.instruction=Instruction()

# Funcion para calcular la distribucion de Poisson
    def Poisson_distribution(self, x, lam=1):
        fact = math.factorial(x)
        prob = (math.pow(lam, x)* math.exp(-lam)) / fact
        return prob
    
    # Funcion para generar numero random siguiendo Poisson
    def __randomPoisson(self, range):

        while True:        
            ind = random.randint(0, range)
            dist = random.uniform(0.0, 1.0)        
            if dist >= self.Poisson_distribution(ind):
                return ind
    
    def __dataGenerate(self):
        hexa=hex(random.randint(0, 65535)) #16 Bits
        #print(hexa)
        return hexa
    
    def generate(self):
        ind=self.__randomPoisson(2)
        self.instruction.set_operation(ind)
        addr=self.__randomPoisson(7)
        if(self.instruction.OPERATION=="WRITE"):
            self.instruction.set_data(self.__dataGenerate())
            self.instruction.set_address(addr)
        if(self.instruction.OPERATION=="READ"):
            self.instruction.set_address(addr)
        return self.instruction



inst=InstructionGenerator()
#inst.dataGenerate()
inst.generate()
print("Operation: ",inst.instruction.OPERATION,"\nData: ",
inst.instruction.DATA,"\nAddr: ",inst.instruction.ADDRESS)