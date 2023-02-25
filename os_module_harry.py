import os

if (not os.path.exists("Data")):
    os.mkdir("Data")

for i in range(10):
    os.mkfifo(f"Data/Day{i+1}.py")
