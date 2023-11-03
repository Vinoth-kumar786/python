class shape():
  def area(self):
       return 0
class Reactangule(shape):
    def area(self):
        l=10
        b=20
        print(l*b)       
r1=Reactangule()
print(r1.area())
###################
class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
     print("name:",self.name,"grade:",self.grade)
     

d1=student("vinoth","s")

d1.display()



     


