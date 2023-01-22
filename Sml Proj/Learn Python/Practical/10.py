#Program 10
num = int(input("Enter a number: ")) #24

sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
        
if sum == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
# Output: 24 is not a perfect number
