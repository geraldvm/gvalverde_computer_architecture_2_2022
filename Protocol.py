from re import search
from Cache import Cache
from CacheBlock import *
from Memory import Memory

class Bus:
    def __init__(self,cache_list, memory):
        self.CACHE_LIST=cache_list
        self.MEMORY=memory
    
    def __copies(self,address):
        n_copies=0
        for cache in self.CACHE_LIST:
            if(cache.exists(address)):
                n_copies+=1
        print("COPIES: "+str(n_copies))
        return n_copies

    # Search cache by ID
    def search_cache(self,ID):
        pos=0
        for cache in self.CACHE_LIST:
            if(cache.ID==ID):
                return pos
            pos+=1
        return -1

    def read(self, ID, address):
        # STATE: Exclusive
        if(0==self.__copies(address)):
            ind = self.search_cache(ID)
            set=self.CACHE_LIST[ind].get_block(address)
            if(set==-1):
                #como no existe
                set=0
            self.CACHE_LIST[ind].BLOCKS[set].STATE='E'
            mem=self.MEMORY.read(address)
            
            if(False!=mem):
                self.CACHE_LIST[ind].BLOCKS[set].TAG=address
                self.CACHE_LIST[ind].BLOCKS[set].DATA=mem.DATA

        print("READ")
        #return 0





mem= Memory(0)
mem.write('0100',0x58)
mem.write('0000',0x58)
#mem.iprint()
cache_list=[Cache("CPU@01"),Cache("CPU@02"),Cache("CPU@03"),Cache("CPU@04")]
bus= Bus(cache_list,mem)
bus.read("CPU@01",'0100')
bus.read("CPU@02",'0000')
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
#bus.copies('0000')
