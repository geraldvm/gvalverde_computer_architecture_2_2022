class MemoryBlock:
    def __init__(self,address):
        self.ADDRESS=address
        self.DATA='0x00'
    
    def get_data(self):
        return self.DATA
    
    def set_data(self,data):
        self.DATA=data
        #if(data>=0x00 and data<=0xFFFF): #16Bits
        #    self.DATA=data
        #else:
        #    print('Error Data out of range')