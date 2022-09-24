from genericpath import exists
from CacheBlock import *

class Cache:
    def __init__(self,ID):
        self.ID=ID
        self.BLOCKS=[CacheBlock(ID,0),CacheBlock(ID,1),CacheBlock(ID,2),CacheBlock(ID,3)]
       
    
    def iprint(self):
        print('¦   ID   ¦  SET  ¦  STATE  ¦    TAG    ¦    DATA    ¦\n')
        for cash in self.BLOCKS:
            print('¦ '+cash.ID+' ¦   '+str(cash.SET)+'   ¦    '+cash.STATE+'    ¦    '+cash.TAG+'   ¦ '+hex(cash.DATA)+' ¦ \n')

    
    def exists(self,address):
        for block in self.BLOCKS:
            if(block.TAG==address):
                return True
        return False
    
    def get_block_id(self,address):
        for block in self.BLOCKS:
            if(block.TAG==address):
                return block.SET
        return -1
    
    def get_block(self,address):
        for block in self.BLOCKS:
            if(block.TAG==address):
                return block
        return -1

    def set_block(self,set,address,data,state):
        for block in self.BLOCKS:
            if(block.SET==set):
                block.TAG=address
                block.DATA=data
                block.STATE=state
        


#cash= Cache("CPU@03")
#cash.iprint()