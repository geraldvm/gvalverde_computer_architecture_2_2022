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
        return -1

    def write(self,address,data):
        sleep(self.__timer)
        for mem in self.block:
            if(mem.ADDRESS==address):
                mem.set_data(data)
                break
    
    def getMemory(self):
        return self.block
    
    def iprint(self):
        for mem in self.block:
            print('¦ '+mem.ADDRESS+': '+hex(mem.DATA)+' ¦\n')

mem= Memory(5)
#mem.set_block('0000',58)
#print(mem.get_block('0000').get_data())
mem.iprint()