import MemoryBlock

class Memory:
    def __init__(self):
        self.block=[MemoryBlock(0),MemoryBlock(1),MemoryBlock(2),MemoryBlock(3),
        MemoryBlock(4),MemoryBlock(5),MemoryBlock(6),MemoryBlock(7)]

    def get_block(self,address):
        return self.block[address]

    def set_block(self,address,data):
        self.block[address].set_data(data)