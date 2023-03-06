s1 = {1, 2, 3, 4}
s2 = {3, 5, 6}

print(s1.union(s2))

s1.update(s2)
print(s1)

print(s1.intersection(s2))

s3 = {1, 2, 3, 4, 5}
s4 = {14, 6, 7}

print(s3.symmetric_difference(s4))
print(s3.isdisjoint(s4))


s5 = {3, 4, 5, 6, 7}
s6 = {3, 5}

print(s5.issuperset(s6))
print(s6.issubset(s5))

cities = {"Mumbai", "Delhi"}
cities.add("Pune")
# cities.remove("Pune")
cities.discard("Pune")
print(cities)


set = {1, 2, 3, 4, 5}
item = set.pop()
print(item)
print()
