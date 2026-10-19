def Max(a,b,c):
    max = a or b or c 
    if(a>b) and  (a>c):
        print("a is largest")
    elif (b>a) and (b>c):
        print("b is largest")
    elif (c>a) and (c>a):
        print(("c is largest"))
    return max
a = int(input("enter value for a "))
b = int(input("enter value for b "))
c = int(input("enter value for c "))
Max(a,b,c)