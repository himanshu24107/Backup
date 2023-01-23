#Program 17
n = int(input("No. of elements in the list:"))
search_num = int(input("Search no:"))
lst = []
for i in range(n):
    j = int(input(f"Enter {i+1} element:"))
    lst.append(j)
for j in lst:
    if j == search_num:
        print(search_num, "is in the list.")
        break
else:
    print(search_num, "is not in the list.")

        


