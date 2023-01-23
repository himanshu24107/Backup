#Program 16
n = tuple(input("Enter Tuple:"))
print(f'Tuple:{n}')
smallest = n[0]
for i in n:
    if i < smallest:
        smallest = i
print("Smallest element:", smallest)

        
