"""To accept a number from user and print digits of number in a reverse order."""

num = int(input("Enter a Number : "))
rev_num = 0
while num > 0:
    digit = num % 10  
    rev_num = rev_num * 10 + digit  
    num //= 10 

print(rev_num)
