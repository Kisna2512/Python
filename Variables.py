class Student:
  def __init__(self):
    self.sname="Krishna" #Instance variable
    self.lnamn="Kotgire"
    self.roll_no=69
    self.branch="CS"
    self.mb=9089764532

  def getdata(self):
    self.age=21

obj=Student()
obj.getdata()
obj.gender="Male"
del obj.sname
print(obj.__dict__)