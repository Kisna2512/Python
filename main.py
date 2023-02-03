#Question1
# for i in range(2,20):
#   print("\t",i)
#   for j in range(1,11):
#     print(f"{i} X {j}=",i*j)
#   print("\t")

# lt=[1,2,4,5]
# lt1=[5,4,2,1]

# print(*zip(lt,lt1))
# for i in range(len(lt)):
#   print(lt[i]," ",lt1[i])
  

# for i in range(1,6):
#   if(i==3):
#     continue
#   else:  
#    print(i," ",6-i)
  
# for i,j ,k in zip(range(1,6),range(5,0,-1),range(11,15)):
#   if(i==3 and j==3):
#     continue
#   else:
#     print(i," ",j," ",k)


# n=ord(input("Enter  chracter: "))
# With inbuilt functions
# if(n.islower()):
#   print("User entered in Lowercase")
# elif(n.isupper()):
#   print("User entered in uppercase")
# elif(n.isdigit()):
#   print("User entered in digit")
# else:
#   print("User entered special chracter")

# # Without inbuilt functions
# if(n >= 65 and n <= 90):
#   print("User entered in uppercase")
# elif(n >=97 and n <= 122):
#   print("User entred in lowercase")
# elif(n >= 48 and n <= 57):
#   print("User entred in digit")
# else:
#   print("User entred in special symbol")

# def login(username,password):
#   while(username!=password):
#     print("Password incorrect")
#     print("Enter correct credentials")
#     username=input("Enter login id: ")
#     password=input("Enter password: ")
#   else:
#     print("Login Succesfully!!")

# lg=input("Enter login: ")
# ps=input("Enter password: ")
# login(lg,ps)



a=int(input("Enter the amount: "))
two=0
five=0
twoh=0
hun=0
tw=0
te=0
ff=0
ft=0
while(a!=0):
  if a%2000==0:
    a-=2000
    two=two+1
  elif a%500==0:
    a-=500
    five=five+1
  elif a%200==0:
    a-=200
    twoh=twoh+1
  elif a%100==0:
    a-=100
    hun+=1
  elif a%50==0:
    a-=50
    ft+=1
  elif a%20==0:
    a-=20
    tw+=1
  elif a%5==0:
    a-=5
    ff+=1
  else:
    a-=10
    te+=1
else:
  print("2000: ",two)
  print("500",five)
  print("200",twoh)
  print("100",hun)
  print("50",ft)
  print("20",tw)
  print("10",te)
  print("5:",ff)
  
    
    