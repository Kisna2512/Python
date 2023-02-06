l = [12, 3, 4, 53, 2]

print(l)
l.append(345)
print(l)
l.sort()
print(l)
# l.sort(reverse=True)
l.reverse()
print(l)
print(l.count(4))
m = l.copy()
m[0] = l[0]
l.insert(1, 8734)
print(l)
mp = [12, 34, 56]
# l.extend(mp)
k = l+mp
print(k)
