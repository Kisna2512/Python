print("******************KBC***************************")
Q = ["Who is the Prime minister of India?\n1.J.Pandit Nehru 2.Narendra Modi 3.Mahatma Gandhi 4.Yogi Adityanath",
     "Which is the Capital of India?\n1.Hyd 2.Delhi 3.Pune 4.Banglore", ]

price = 0
for i in Q:
    print(i)
    a = int(input("Choose the correct option to win prices: "))
    if(a == 2):
        price += 200

print("The price you have won is ", price, "rs")
