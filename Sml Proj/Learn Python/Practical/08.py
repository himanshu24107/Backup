#Program 8
n = int(input("Enter a number: "))
m = n
sum = 0
num_of_digits = len(str(n))
while m > 0:
    digit = m % 10
    sum += digit ** num_of_digits
    m = m// 10
if n == sum:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
