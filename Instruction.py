class Instruction:
    def __init__(self, processor_id):
        self.__operations=["READ", "WRITE","CALC"]
        self.__mem_addr=['0000','0010','0100','0110','1000','1010','1100','1110','-1']
        self.OPERATION=''
        self.DATA=-1
        self.ADDRESS='-1'
        self.PROC_ID=processor_id
        
    
    def set_operation(self, ind):
        self.OPERATION=self.__operations[ind]

    def set_address(self, address):
        self.ADDRESS=self.__mem_addr[address]
    
    def set_data(self, data):
        self.DATA=data

    def iprint(self):
        if(self.OPERATION=="WRITE"):
            print(self.OPERATION+' '+self.ADDRESS+';'+self.DATA)
        elif(self.OPERATION=="READ"):
            print(self.OPERATION+' '+self.ADDRESS)
        else:
            print(self.OPERATION)
    
    def istring(self):
        if(self.OPERATION=="WRITE"):
            hexa=hex(self.DATA)
            return self.OPERATION+' '+self.ADDRESS+';'+self.DATA
        elif(self.OPERATION=="READ"):
            return self.OPERATION+' '+self.ADDRESS
        else:
            return self.OPERATION

    def read(self, address):
        self.OPERATION="read"
        self.DATA=0x0
        self.ADDRESS=address

    def write(self, address, data):
        self.OPERATION="write"
        self.DATA=data
        self.ADDRESS=address

    def calc(self):
        self.OPERATION="calc"
        self.DATA=0x0
        self.ADDRESS=0000
        print("CALC")
        return 0
