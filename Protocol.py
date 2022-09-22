from Cache import Cache
from CacheBlock import *

class Bus:
    def __init__(self,Cache):
        self.CACHE_01=Cache[0]
        self.CACHE_02=Cache[1]
        self.CACHE_03=Cache[2]
        self.CACHE_04=Cache[3]
    
    def __copies(self,address):
        n_copies=0
        if (self.CACHE_01.exists(address)):
            n_copies+=1
        if (self.CACHE_02.exists(address)):
            n_copies+=1
        if (self.CACHE_03.exists(address)):
            n_copies+=1
        if (self.CACHE_04.exists(address)):
            n_copies+=1
        print("COPIES: "+str(n_copies))
        return n_copies



cache_list=[Cache("CPU@01"),Cache("CPU@02"),Cache("CPU@03"),Cache("CPU@04")]
bus= Bus(cache_list)

bus.copies('0000')