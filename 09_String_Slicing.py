# String Slicing ans operations on string

name = "Krishna,Aniket"

# Square brackets are used for slicing in Python
# for finding the length of string
print("length of the string is: ", len(name))
print(name[0:7])  # It will take index upto n-1 from [0:n]

fruit = "Mango"

print(fruit[:4])
print(fruit[1:4])
print(fruit[0:-3])  # it is equivalent to the fruit[0:len(fruit)-3]=fruit[0:2]
print(fruit[-3:-1])


for ch in name:
    print(ch, end="")
