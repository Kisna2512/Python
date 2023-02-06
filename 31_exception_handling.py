a = input("Enter the number: ")


print(f"Multiplication table of {a}:")
try:
    for i in range(11):
        print(a, "x", i, "=", int(a)*i)

except Exception as e:
    print(e)

print("Program Ends here")
