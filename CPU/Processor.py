class Processor:
    def __init__(self,id):
        self.ID=id
    
    def calc(self):
        print(self.ID+": Calc()")
    
    def write(self,address,data):
        print("WRITE DATA "+data+" IN ADDRESS "+address)

    def read(self,address):
        print("READ ADDRESS "+address)

#cpu_01=Processor("CPU@01")
#cpu_01.calc()