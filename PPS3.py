"""To accept N numbers from user. Compute and display maximum in list,
minimum in list, sum and average of numbers."""
arr = []
n = 0 
avg = 0
print("Enter the numbers : ")
while True :
   N = input()
   if N == "":
       break
   N = int(N)
   arr.append(N)

    
print(arr)

print("Maximum Value is : ", max(arr))# To calculate Maximum Value 
print("Minimum Value is : ", min(arr))# TO calculate Minimum Value
for i in arr:# To calculate the Sum of the numbers
    n = n + int(i)
print("Sum of Elements is : " , n)


avg = n/len(arr)
print("The average of the number is : ", avg )