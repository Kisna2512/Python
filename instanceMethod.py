class Student:
  def __init__(self,name,age,roll_no):
    self.name=name
    self.age=age
    self.roll_no=roll_no



  def display(self): #Instance method
    print(self.name," ",self.age," ",self.roll_no)

obj=Student("Krishna",21,7)
obj.display()
    
  