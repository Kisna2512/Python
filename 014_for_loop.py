name = "Krishna"

for i in name:
    print(i, end=",")
    if(i == 'b'):
        print("This is something b")

print()
colors = ["Red", "Green", "Blue", "Yellow"]


for color in colors:
    print(color, end=" ")
    for i in color:
        print(i, end=",")
print()
# Range function will go till n-1
for i in range(0, 11):
    print(i)


for i in range(0, 10, 2):
    print(i)
