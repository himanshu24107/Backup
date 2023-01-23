#Program 18
n = int(input("No. of elements in the list:"))
lst = []
for i in range(n):
    k = int(input(f"Enter {i+1} element:"))
    lst.append(k)
reversed_list = []
for i in range(len(lst)-1, -1, -1):
    reversed_list.append(lst[i])
print("Original list:", lst)
print("Reversed list:", reversed_list)
