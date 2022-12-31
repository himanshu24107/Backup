n = int(input("Enter a number: "))
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