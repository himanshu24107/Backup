lst = []
def result():
    print(f'{x} is largest')
def addlst(n):
    lst.append(n)
for i in range(0,3):
    n = int(input("Enter numbers: "))
    addlst(n)

lst.sort()
x = lst[-1]
result()

