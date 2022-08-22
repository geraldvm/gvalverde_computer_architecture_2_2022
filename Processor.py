from audioop import add


class Processor:
    def __init__(self,id):
        self.id=id
    
    def calc(self):
        print("Calc")
    
    def write(self,address,data):
        print("WRITE DATA "+data+" IN ADDRESS "+address)

    def read(self,address):
        print("READ ADDRESS "+address)

    