# Types of argument
# 1.Default Argument
# 2.keyword Argument
# 3.Variable length argument
# 4.Required Argument

# function with default argument
def average(a, b=4):
    print(a)
    print(b)
    print("The Average is:", (a+b)/2)


average(a=21, b=4)

# keyword argument
average(b=45, a=3)


# Required Argument
average(a=56)

# Variable length argument

# this function is taking the numbers as tuple


def sum(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Sum of variable length argument is:", sum)


# Variable length arguments
sum(1, 2, 3, 4, 5)

# This function taking argument as a dictionary


def printname(**name):
    print(type(name))
    print(name["fname"], " ", name["lname"])


printname(fname="krishna", lname="Kotgire")


def greet():
    return "Good night"


print(greet())
