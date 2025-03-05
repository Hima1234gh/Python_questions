import math

num = float(input("Enter The Number "))

if num < 0:
    print("The Squre of a number cannot be negative")
else:
    print(f"The Square Roote of the {num} is {math.sqrt(num)}")

print(f"Square of the {num} is {num*num}")

print(f"Cube of {num} is {num**3}")

if num < 0:
    print("Prime numbers cannot be negative")
else:
    if num % 2 == 0 :
        print(f"{num} is not Prime")
    else :
        print(f"{num} is PRIME")



def factorial_num(n) :
   
    if n < 0 :
        return "Factorial is only defined for Positive integers"
     
    n = int(n)
    if n == 1 or n == 0 :
        return 1
    else:
        return n*factorial_num(n-1)
    
print(f"The factorial of the {num} is {factorial_num(num)}")

def prime_factor(num):
    factor = []
    if num < 0:
        factor.append(-1)
        num = abs(num)
   

    while num%2 == 0 :
        factor.append(2)
        num //= 2
    
    i = 3 
    while i*i <= num :
        while num%i == 0 :
            factor.append(i)
            num //= i
        i +=2
    
    if num > 2:
        factor.append(num)
    
    return factor

print(prime_factor(num))
