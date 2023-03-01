x = 4


def hello():
    x = 5
    y = 1
    print(f"The local variable x is {x}")


print(f"The global varibale x is {x}")
hello()
print(f"The global varibale x is {x}")
print(y)
