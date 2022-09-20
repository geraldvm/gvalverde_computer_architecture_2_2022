import MemoryBlock

class Memory:
    def __init__(self):
        self.block=[MemoryBlock('0000'),MemoryBlock('0010'),MemoryBlock('0100'),MemoryBlock('0110'),
        MemoryBlock('1000'),MemoryBlock('1010'),MemoryBlock('1100'),MemoryBlock('1110')]

    def get_block(self,address):
        return self.block[address]

    def set_block(self,address,data):
        self.block[address].set_data(data)