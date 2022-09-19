class Instruction:
    def __init__(self):
        self.cpu=0
        self.operation=""
        self.data=0x0
        self.address=0000

    def read(self, cpu, address):
        self.cpu=cpu
        self.operation="read"
        self.data=0x0
        self.address=address

    def write(self, cpu, address, data):
        self.cpu=cpu
        self.operation="write"
        self.data=data
        self.address=address

    def calc(self,cpu):
        self.cpu=0
        self.operation="calc"
        self.data=0x0
        self.address=0000
        print("CALC")
        return 0
