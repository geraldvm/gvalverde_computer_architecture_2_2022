import CacheBlock

class Cache:
    def __init__(self,ID):
        self.ID=ID
        self.BLOCKS=[CacheBlock(ID,0),CacheBlock(ID,1),CacheBlock(ID,2),CacheBlock(ID,3)]
        print("Cache")