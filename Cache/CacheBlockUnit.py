class CacheBlockUnit:
    def __init__(self, block_number):
        self.NUMBER=block_number
        self.COHERENCY='S'
        self.MEMORY_ADDRESS=block_number
        self.DATA=0
    
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