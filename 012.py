import time

name = input("Enter your name:")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
h = int(time.strftime('%H'))
if(h < 12):
    print(f'Good Morning {name}')
elif(h >= 12 and h < 18):
    print(f"Good Afternoon {name}")
elif(h >= 18 and h < 20):
    print(f"Good evening {name}")
else:
    print(f"Good night {name}")
