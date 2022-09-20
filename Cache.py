import CacheBlock

class Cache:
    def __init__(self,ID):
        self.ID=ID
        self.BLOCKS=CacheBlock(ID)
        print("Cache")