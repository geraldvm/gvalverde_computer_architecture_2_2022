class MemoryBlock:
    def __init__(self,address):
        self.address=address
        self.data=0
    
    def get_data(self):
        return self.data
    
    def set_data(self,data):
        self.data=data