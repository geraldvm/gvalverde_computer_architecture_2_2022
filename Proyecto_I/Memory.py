from MemoryBlock import *
from time import sleep

class Memory:
    def __init__(self,timer):
        self.block=[MemoryBlock('0000'),MemoryBlock('0010'),MemoryBlock('0100'),MemoryBlock('0110'),
        MemoryBlock('1000'),MemoryBlock('1010'),MemoryBlock('1100'),MemoryBlock('1110')]
        self.__timer=timer

    def read(self,address):
        for mem in self.block:
            if(mem.ADDRESS==address):
                sleep(self.__timer)
                return mem
        return False

    def write(self,address,data):
        sleep(self.__timer)
        for mem in self.block:
            if(mem.ADDRESS==address):
                mem.set_data(data)
                return True
        return False
    
    def getMemory(self):
        return self.block
    
    def getMemory(self, address):
        pos=0
        for mem in self.block:
            if(mem.ADDRESS==address):
                return pos
            pos+=1
        return False
    
    def iprint(self):
        for mem in self.block:
            print('¦ '+mem.ADDRESS+': '+hex(mem.DATA)+' ¦\n')

    def istring(self):
        result=['¦  ADDRESS  ¦  DATA    ¦\n']
        for mem in self.block:
            temp='¦ '+mem.ADDRESS+'    ¦    '+mem.DATA+' ¦\n'
            result+=[temp]
        return result

#mem= Memory(5)
#mem.set_block('0000',58)
#print(mem.get_block('0000').get_data())
#mem.iprint()