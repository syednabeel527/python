def Even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
    return
a = int(input("Enter value for A "))
b = int(input("Enter value for B "))
Even(a,b) 