n=int(input("Enter the no of rows: "))


for i in range(0,n):
  for j in range(0,n):
    print("*",end=" ")
  print()  


for i in range(0,n):
  for j in range(0,n):
    print(f"{chr(64+i+1)}",end=" ")
  print()  

