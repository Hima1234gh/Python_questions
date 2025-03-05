print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication")
print("4.Division")
print("5.Power (x^y)")
print("6.Factorial(!)")
operation = int(input("Enter the operation Your Have to do : "))

if operation <= 6 :
    if operation == 1 :
        a = float(input("Enter First Number : "))
        b = float(input("Enter Second Number : "))
        print( a + b)
    elif operation == 2:
        a = float(input("Enter First Number : "))
        b = float(input("Enter Second Number : "))
        if a > b :
            sub = a - b
        elif a < b :
            sub = b - a
        print(sub)
    elif operation == 3 :
        a = float(input("Enter First Number : "))
        b = float(input("Enter Second Number : "))
        mult = a * b
        print(mult)
    elif operation == 4 :
        a = float(input("Enter Numerator"))
        b = float(input("Enter Denominator"))
        if b != 0 :
            print(a/b)
        else:
            print("Invalide Operation")
    elif operation == 5 :
        a = float(input("Enter Number : "))
        b = float(input("Enter the Power Of The Number : "))
        print(f"{a} to the power {b} = {a**b}")
    else :
        a = float(input("Enter  Number : "))
        def factorial(n):
            if n == 0 or n == 1 :
                return 1
            else :
                return n*factorial(n-1)
        result = factorial(a)
        print(result)
else:
    print("Invalide Operation")
