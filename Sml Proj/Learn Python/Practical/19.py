#Program 19
n = int(input("No. of elements in the list:"))

lst = []
for i in range(n):
    k = int(input(f"Enter {i+1} element:"))
    lst.append(k)

for i in range(0, len(lst)-1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]

print("Swapped list:", lst)
