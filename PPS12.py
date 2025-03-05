"""To input binary number from user and convert it into decimal number."""

binary = str(input("Enter the Binary Code og The Number : "))

def binary_to_decimal(n):
    binary = 0
    power = 0
    for digit in reversed(n):
        if digit == "1":
            binary += 2**power
        elif digit != "0":
            return "Invalid Entry"
        power+=1

    return binary

print(binary_to_decimal(binary))
        

# def binary_to_decimal(n):
#     try:
#         decimal = int(n, 2)
#         return decimal
#     except ValueError:
#         return "The Number is Invalid"

# print(binary_to_decimal(str(binary)))
