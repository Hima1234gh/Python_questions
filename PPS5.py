"""To check whether input number is Armstrong number or not. An Armstrong
number is an integer with three digits such that the sum of the cubes of its digits
is equal to the number itself. Ex. 371."""

num = int(input("Enter a Three Digit Number : "))

def armstrong_num(num):
    sum_of_cube_of_num = 0
    if len(str(num)) == 3 :
        for i in str(num):
            sum_of_cube_of_num  += int(i)**3
        if sum_of_cube_of_num == num:
            print(f"{num} is a Armstrong Number")
        else:
            print(f"{num} is not a Armstrong Number")
    else :
        print("Invalid Number")

armstrong_num(num)