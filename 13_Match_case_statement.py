# It is like Switch case statement in Python
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("value of x is zero")
    case 1:
        print("value of x is one")
    case _ if x != 90:
        print(x, "is not 90")
    case _:
        print("The value of x is:", x)
