def table(n):
    tab = 1
    for i in range(1,11):
        tab = n*i
        print(tab)
n = int(input("Enter the value for n "))
table(n)