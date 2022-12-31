lst = []
def result():
    print(f'{x} is largest')
def addlst(n):
    lst.append(n)

n = int(input("Enter first number: "))
addlst(n)
n = int(input("Enter Second number: "))
addlst(n)
n = int(input("Enter Third number: "))
addlst(n)

lst.sort()
x = lst[-1]
result()

