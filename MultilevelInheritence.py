class Login:
  def __init__(self):
    self.id=input("Enter your login id: ")
    self.password=input("Enter your password: ")
    if(self.id==self.password):
      print("Login Succesfull")
    else:
      # print("Login Failed")
      raise Exception("Login Failed")

class College(Login):
  def __init__(self):
    Login.__init__(self)
    self.college_name=input("Enter your college name: ")
    self.branch= input("Enter your branch name: ")
    match self.branch:
        case "CS":
          self.CS()
        case "ENTC":   
          self.ENTC()
        case "IT":
          self.IT()



  def CS(self):
    try:
       self.sub1=int(input("Enter your marks in TOC: "))
       self.sub2=int(input("Enter your marks in DBMS: "))
       self.sub3=int(input("Enter your marks in OS: "))
       self.sub4=int(input("Enter your marks in DSA: "))
       self.sub5=int(input("Enter your marks in CNS: "))
       self.calc(self.sub1,self.sub2,self.sub3,self.sub4,self.sub5)
    except ValueError as msg:
      print(msg)


  def IT(self):
    try:
       self.sub1=int(input("Enter your marks in TOC: "))
       self.sub2=int(input("Enter your marks in DBMS: "))
       self.sub3=int(input("Enter your marks in OS: "))
       self.sub4=int(input("Enter your marks in DSA: "))
       self.sub5=int(input("Enter your marks in CNS: "))
       self.calc(self.sub1,self.sub2,self.sub3,self.sub4,self.sub5)
    except ValueError as msg:
      print(msg)



  def ENTC(self):
    self.sub1=int(input("Enter your marks in DC: "))
    self.sub2=int(input("Enter your marks in MC: "))
    self.sub3=int(input("Enter your marks in DBMS: "))
    self.sub4=int(input("Enter your marks in EM: "))
    self.sub5=int(input("Enter your marks in JAVA: "))
    self.calc(self.sub1,self.sub2,self.sub3,self.sub4,self.sub5)
    


  def calc(self,sub1,sub2,sub3,sub4,sub5):
    per=((self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)/500)*100
    print("====================================================")
    print(f"\t\t\t\t\tCollege Name:{self.college_name}\t\t\t\t\t")
    print("=====================================================")
    print(f"\n\t\t\t\t\tBranch:{self.branch}\n")
    print("=====================================================")
    if(self.branch=="CS"):
      print(f"\t\t\t\t|\tTOC:\t{self.sub1} |")
      print(f"\t\t\t\t|\tDBMS:\t{self.sub2} |")
      print(f"\t\t\t\t|\tOS :\t{self.sub3} |")
      print(f"\t\t\t\t|\tCNS:\t{self.sub4} |")
      print(f"\t\t\t\t|\tDSA:\t{self.sub5} |")  
    print("Your Percentage is: ",per)
    if(per < 35):
      print("You are fail")
    else:
      print("You are pass")


class result(College):
  def __init__(self):
   College. __init__(self)
    
      


obj=result()

  

    
    
          



    
    
    
     