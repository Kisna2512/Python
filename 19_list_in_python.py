marks = [19, 20, 3, 1]
print(marks)
print(type(marks))

print(marks[0])
# List are changeble means mutable

for i in marks:
    print(i)


l = [12, "krishna", "Yash", 34.5]
# print(l)
print(l[-3])  # =len(l)-3

if "lri" in "krishna":
    print("Yes")
else:
    print("NO")


print(l[1:4])
print(l[0:4:2])  # Third is jump index


# List comprhension
lst = [i * i for i in range(11)]
print(lst)
