a = "Krishna"
# Strings are immmutable in Python
print(len(a))

print(a.upper())  # Convert the string to uppercase
print(a.lower())  # Convert the string to lowercase
print(a)

b = "Krishna!!!!"
print("Printing the output without trailing !:", b.rstrip("!"))
print(b.replace("Krishna", "Yash"))

c = "krishna is very good at coding"
print(c.split(" "))  # It will Split into list

heading = "introduction to python"
# It will convert first leeter of string into uppercase
print(heading.capitalize())

print(heading.center(50))

print(heading.count("t"))  # It will Count the occurences

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
print(str1.endswith("to"))

print(str1.find("th"))


num = "23asde"
print(num.isalnum())  # It will specify is your string is alphanumeric or not

str1 = "kllool"
print(str1.isalpha())
str2 = "Welcome"
print(str1.islower())
print(str2.isprintable())


str3 = "      "
print(str3.isspace())

str4 = "world"
print(str4.istitle())
print(str4.startswith("w"))
print(str4.swapcase())


str5 = "He is mine you"
print(str5.title())
