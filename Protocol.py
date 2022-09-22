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
    def __search_cache(self,ID):
        pos=0
        for cache in self.CACHE_LIST:
            if(cache.ID==ID):
                return pos
            pos+=1
        return -1
    
    def read(self, ID, address):
        #STATE: EXCLUSIVE
        if(0==self.__copies(address)):
            self.__read_exclusive(ID, address)
        elif(0<self.__copies(address)):
            self.__read_shared(ID, address)

    def __read_exclusive(self, ID, address):
        # STATE: Exclusive
        ind = self.__search_cache(ID)
        set=self.CACHE_LIST[ind].get_block(address)
        if(set==-1):
            #como no existe
            set=0
        self.CACHE_LIST[ind].BLOCKS[set].STATE='E'
        mem=self.MEMORY.read(address)
        
        if(False!=mem):
            self.CACHE_LIST[ind].BLOCKS[set].TAG=address
            self.CACHE_LIST[ind].BLOCKS[set].DATA=mem.DATA
    
    def __search_data_other_cache(self,ID, address):
        pos=0
        positions_list=[]
        for cache in self.CACHE_LIST:
            if(cache.ID!=ID):
                if(cache.exists(address)):
                    positions_list+=[pos]
            pos+=1
        return positions_list

    def __read_shared(self, ID, address):
        # STATE: Shared
        positions_list = self.__search_data_other_cache(ID,address)
        ind = self.__search_cache(ID)
        for pos in positions_list:
            set=self.CACHE_LIST[pos].get_block(address)
            self.CACHE_LIST[pos].BLOCKS[set].STATE='S'
            self.CACHE_LIST[pos].BLOCKS[set].TAG=address
            data=self.CACHE_LIST[pos].BLOCKS[set].DATA
        set=self.CACHE_LIST[ind].get_block(address)
        self.CACHE_LIST[ind].BLOCKS[set].STATE='S'
        self.CACHE_LIST[ind].BLOCKS[set].DATA=data
        self.CACHE_LIST[ind].BLOCKS[set].TAG=address
        
        





mem= Memory(0)
mem.write('0100',0x58)
mem.write('0000',0x58)
#mem.iprint()
cache_list=[Cache("CPU@01"),Cache("CPU@02"),Cache("CPU@03"),Cache("CPU@04")]
bus= Bus(cache_list,mem)
bus.read("CPU@01",'0100')

bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
print("***************#2**********************************")
bus.read("CPU@02",'0100')
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
bus.read("CPU@03",'0100')
print("***************#3**********************************")
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
bus.CACHE_LIST[2].iprint()
#bus.copies('0000')
