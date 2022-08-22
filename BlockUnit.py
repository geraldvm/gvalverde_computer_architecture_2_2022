class BlockUnit:
    def __init__(self, ID):
        self.ID=ID
        self.COHERENCY='S'
        self.MEMORY_ADDRESS=ID
        self.DATA=0
    
    def set_data(self,data):
        self.DATA=data
    
    def get_data(self):
        return self.DATA
    
    def set_coherency(self,state):
        self.COHERENCY=state
    
    def get_coherency(self):
        return self.COHERENCY