
from audioop import add
from zlib import DEF_BUF_SIZE


class Instruction:
    def __init__(self):
        self.CPU=0
        self.__operations=["READ", "WRITE","CALC"]
        self.__mem_addr=['0000','0010','0100','0110','1000','1010','1100','1110']
        self.OPERATION=''
        self.DATA=-1
        self.ADDRESS='-1'
    
    def set_operation(self, ind):
        self.OPERATION=self.__operations[ind]

    def set_address(self, address):
        self.ADDRESS=self.__mem_addr[address]
    
    def set_data(self, data):
        self.DATA=data

    def read(self, cpu, address):
        self.CPU=cpu
        self.OPERATION="read"
        self.DATA=0x0
        self.ADDRESS=address

    def write(self, cpu, address, data):
        self.CPU=cpu
        self.OPERATION="write"
        self.DATA=data
        self.ADDRESS=address

    def calc(self,cpu):
        self.CPU=0
        self.OPERATION="calc"
        self.DATA=0x0
        self.ADDRESS=0000
        print("CALC")
        return 0
