def calculateGmean(a, b):
    return (a*b)/(a+b)


def isGreater(a, b):
    if(a > b):
        print("first number is greater")
    else:
        print("Second number is greater or equal")


def isLessser(a, b):
    pass


a = 8
b = 9

gmean = (a*b)/(a+b)
print(gmean)
isGreater(a, b)

c = 5
d = 3

print(calculateGmean(c, d))
