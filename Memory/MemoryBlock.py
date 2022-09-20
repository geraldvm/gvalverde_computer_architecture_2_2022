class MemoryBlock:
    def __init__(self,address):
        self.ADDRESS=address
        self.DATA=0
    
    def get_data(self):
        return self.DATA
    
    def set_data(self,data):
        self.DATA=data