# Program 7
n = int(input("Enter a number: "))#6996
m = n
s = 0
while n>0:
    i = n%10
    n = n//10
    s = s*10+i
    # print(i,end='')

if s==m:
    print(f'{m} is a Palidrome Number.')
else:
    print('Better Luck next time!')
#Output: 6996 is a Palidrome Number.
