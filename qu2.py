list1=["rises","sun","tomato","python"]
k=0

for i in list1:
  str1=""
  str2=""
  for j in i:
    if(j in "aeiouAEIOU"):
      str1+=j
    else:
      str2+=j
  list1[k]=str2+str1 
  k=k+1
     
print(list1)    


