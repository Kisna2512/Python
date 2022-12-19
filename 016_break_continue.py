
# Break statement break the loop
for i in range(1, 12):
    if(i == 5):
        print("Skipeed the iteration", 5)
        continue
    print("5 X ", i, "=", 5*i)
    if(i == 10):
        break
# continue statement skip the present iteration


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in l:
    if(i % 2):
        continue
    print(i, end=" ")
