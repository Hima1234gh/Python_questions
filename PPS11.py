# To accept list of N integers and partition list into two sub lists even and odd
# numbers.


arr = []
print("Enter the numbers with spaces : ")

while True :
    num = input()
    if num == "":
        break
    arr.append(int(num))

print("Your Entered Numbers Are", arr)

evev_num = []
odd_num = []

for i in arr:
    evev_num.append(i) if i%2==0 else odd_num.append(i)

print("The even numbers are : ", evev_num)
print("The odd numbers are : ", odd_num)