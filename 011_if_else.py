age = int(input("Enter your age: "))
print("Your age is:", age)

if age >= 18:
    print("You can drive")
else:
    print("You cannot drive")

# Conditional Operator
# >,<,>=,<=,!=,==

print(age > 18)
print(age == 18)
print(age != 18)
print(age < 18)
print(age <= 18)
print(age >= 18)


applePrice = 210
budget = 200

if(applePrice <= budget):
    print("Alexa,add 1kg apple to the cart!!")
else:
    print("Alexa do not add apple to the cart!!")


num = 0


if num == 1:
    print("Your number is 1")
elif num == 0:
    print("Your number is zero")
else:
    print("Your number is not 0 and 1")


num = int(input("Enter your number:"))
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Your number is between 11-20")
    else:
        print("Your number is greater than 20")
else:
    print("Your number is zero")
