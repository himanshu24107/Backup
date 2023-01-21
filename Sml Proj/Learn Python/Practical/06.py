# Program 6
import math
x = int(input("Enter base no.: "))#5
n = int(input("Enter Degree: "))#2
s = 0
formula = "S = 1-x+x^2-x^3.......x^n"
print(f'Formula: {formula}')

for i in range(0,n+1):
    j = math.pow(x,i)
    if i%2!=0: 
        s = s-j
    else:
        s = s+j
print(f'Answer: {s}')
# Output:Answer 21

