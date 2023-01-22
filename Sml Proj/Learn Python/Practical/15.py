#Program 15
n = int(input("No. of elements in the list:"))
lst = []
for i in range(n):
    j = int(input(f"Enter {i+1} element:"))
    lst.append(j)
lst.sort()
s = lst[0]
print(f'Smallest element: {s}')
        
