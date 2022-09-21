import CacheBlockUnit

class CacheBlock:
    def __init__(self, ID, SET):
        self.ID=ID
        self.COHERENCY='S'
        self.SET=SET
        self.TAG='0000'
        self.DATA=0

    def get_blocks(self):
        return self.BLOCKS
    
    def get_block(self,block_number):
        return self.BLOCKS[block_number]
    
    def set_data(self,data):
        self.DATA=data
    
    def get_data(self):
        return self.DATA
    
    def set_coherency(self,state):
        self.COHERENCY=state
    
    """
    Estado de coherencia: M (modificado), S (shared), I (inv´alido), E (exclusive).
    """
    def get_coherency(self):
        return self.COHERENCY
