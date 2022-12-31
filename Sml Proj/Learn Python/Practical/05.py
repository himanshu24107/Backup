import math
x = int(input("Enter base no.: "))
n = int(input("Enter Degree: "))
s = 0
formula = "S = 1+x+x^2.......x^n"
print(f'Formula: {formula}')

for i in range(0,n+1):
    j = math.pow(x,i)
    s = s+j
print(f'Answer: {s}')


