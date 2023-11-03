class laptop():
    chargertype="C TYPE"

    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
@classmethod
def changechargertype(cls):
    print("change the charger to b")

computer=laptop()
computer.setprice(20000)
