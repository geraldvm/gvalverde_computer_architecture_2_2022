from CacheBlock import *

class Cache:
    def __init__(self,ID):
        self.ID=ID
        self.BLOCKS=[CacheBlock(ID,0),CacheBlock(ID,1),CacheBlock(ID,2),CacheBlock(ID,3)]
        print("Ca$h Memory")
    
    def iprint(self):
        print('¦   ID   ¦  SET  ¦  STATE  ¦    TAG    ¦    DATA    ¦\n')
        for cash in self.BLOCKS:
            print('¦ '+cash.ID+' ¦   '+str(cash.SET)+'   ¦    '+cash.STATE+'    ¦    '+cash.TAG+'   ¦ '+hex(cash.DATA)+' ¦ \n')

cash= Cache("CPU@03")
cash.iprint()