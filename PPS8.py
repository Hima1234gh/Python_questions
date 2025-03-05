"""To accept two numbers from user and compute smallest divisor and Greatest
Common. Divisor of these two numbers."""

a, b = float(input("Enter First Number : ")),float(input("Enter Second Number : "))

def scd(n):
    if n%2 == 0 :
        return 2
    
    for i in range(3, n**0.5, 2):
        if n % i == 0:
            return i 
        
    return n 

if scd(a) == scd(b):
    print(f"The Smallest Common Divisor is {scd(a)}")
else :
    print("There is no Smallest common Divisor")

def gcd(a, b):
    while b != 0 :
        a , b = b , a % b 
    return a 

print(f"The Greatest Common Divisor is {gcd(a, b)}")

