from Cache import Cache
from Memory import Memory
from MemoryBlock import *
from time import sleep

class Controller:
    def __init__(self,ID, memory, cache):
        self.memory=memory
        self.CACHE=cache
        self.ID=ID
        self.__load()

    def __calc_set(self,block_mem):
        set=block_mem%(len(self.CACHE.BLOCKS))
        return set

    def __load(self):
        for i in range(len(self.CACHE.BLOCKS)):
            set=self.__calc_set(i)
            block_mem=self.memory.block[i]
            self.CACHE.set_block(set,block_mem.ADDRESS,block_mem.DATA,'S')

            



mem= Memory(0)
mem.write('0100',0x58)
mem.write('0000',0x969)
#mem.iprint()
cache_list=[Cache("CPU@01"),Cache("CPU@02"),Cache("CPU@03"),Cache("CPU@04")]

cache_list[0].iprint()

controller = Controller("CPU@01",mem,cache_list[0])
print("-----------------------------------------")
cache_list[0].iprint()
print("-----------------------------------------")
cache_list[0].iprint()