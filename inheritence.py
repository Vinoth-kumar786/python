class a():
    def __init__(self): #constructor
        print("hello")
    def displays(self):
        print("a")
class b(): #inheritence
    def __init__(self):
       super().__init__() #super keyword    
       print("hello")
    def display(self):
        print("B")
class c(b,a): #inheritence
    def __init__(self):
       super().__init__() #super keyword
       print("vanakkam")
    def display(self):
        print("c")        
com=c()
