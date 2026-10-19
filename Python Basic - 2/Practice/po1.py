salary = int(input("Enter your salary : "))
if salary < 30000:
    print("5% tax")
elif salary >= 30000 and salary <= 70000 :
    print("15% tax")
elif salary > 75000:
    print("25% tax")