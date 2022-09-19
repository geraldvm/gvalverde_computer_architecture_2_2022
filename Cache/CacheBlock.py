import CacheBlockUnit

class CacheBlock:
    def __init__(self, ID):
        self.ID=ID
        self.BLOCKS=[CacheBlockUnit(0),CacheBlockUnit(1),CacheBlockUnit(2),CacheBlockUnit(3)]

    def get_blocks(self):
        return self.BLOCKS
    
    def get_block(self,block_number):
        return self.BLOCKS[block_number]
