from MemoryBlock import *

class Memory:
    def __init__(self):
        self.block=[MemoryBlock('0000'),MemoryBlock('0010'),MemoryBlock('0100'),MemoryBlock('0110'),
        MemoryBlock('1000'),MemoryBlock('1010'),MemoryBlock('1100'),MemoryBlock('1110')]

    def get_block(self,address):
        for mem in self.block:
            if(mem.ADDRESS==address):
                return mem
        return -1

    def set_block(self,address,data):
        for mem in self.block:
            if(mem.ADDRESS==address):
                mem.set_data(data)
                break

mem= Memory()
mem.set_block('0000',58)
print(mem.get_block('0000').get_data())