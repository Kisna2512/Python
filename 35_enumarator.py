marks = [12, 56, 34, 67]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 2):
        print("Passing")


for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 2):
        print("Passing")
