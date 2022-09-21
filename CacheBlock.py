class CacheBlock:
    def __init__(self, ID, SET):
        self.ID=ID
        self.STATE='S'
        self.SET=SET
        self.TAG='0000'
        self.DATA=0

    def read(self, address):
        if (self.TAG==address):
            return self.DATA
    
    def write(self,address, data):
        self.DATA=data
        self.TAG=address
    
    
    def set_coherency(self,state):
        self.STATE=state
    
    """
    Estado de coherencia: M (modificado), S (shared), I (inv´alido), E (exclusive).
    """
    def get_coherency(self):
        return self.COHERENCY
