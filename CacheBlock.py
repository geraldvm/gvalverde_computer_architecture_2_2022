class CacheBlock:
    def __init__(self, ID, SET):
        self.ID=ID #Processor associative
        self.SET=SET #Block Number
        self.STATE='S' #Coherency state
        self.TAG='1111' #Memory Address
        self.DATA=0x0 #16 Bits Data

    def read(self, address):
        if (self.TAG==address):
            return self.DATA
    
    def write(self,address, data):
        self.DATA=data
        self.TAG=address
    
    def write_miss(self):
        print("write_miss L1 at set"+self.SET+" in "+self.ID)
    
    def read_miss(self):
        print("read_miss L1 at set "+self.SET+" in "+self.ID)
    
    
    def set_coherency(self,state):
        self.STATE=state
    
    """
    Estado de coherencia: M (modificado), S (shared), I (inv´alido), E (exclusive).
    """
    def get_coherency(self):
        return self.COHERENCY
