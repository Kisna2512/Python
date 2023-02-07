class NewClass:
  def __init__(self):#Constuctor 
    print("My name is Constrctor")


  def show(self):
    print("Welcome to class level programming")


obj=NewClass()
obj.show()
print(type(obj))


class HOD:
  def __init__(self,name,age,roll_no): #Parametrized Constructor
    self.name=name
    self.age=age
    self.roll_no=roll_no


  def show(self):
    print("Name: ",self.name)
    print("Age: ",self.age)
    print("Roll no: ",self.roll_no)
    


obj1=HOD("Krishna",21,7)
obj1.show()