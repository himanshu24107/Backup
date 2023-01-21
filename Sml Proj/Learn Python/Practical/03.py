# Program 3
lst = []
def result():
    print(f'{x} is largest.')

for i in range(0,3):
    n = int(input("Enter numbers: ")) #1, 2, 3
    lst.append(n)

lst.sort()
x = lst[-1]
result()
#Output: 3 is largest.
