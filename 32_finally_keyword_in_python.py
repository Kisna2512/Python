try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("I'm always excuated")

    
    
def fun():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 0
    except:
        print("Some error occured")
        return 1

    finally:
        print("I'm always excuated")


x = fun()
print(x)
