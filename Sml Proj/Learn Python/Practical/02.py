#Program 2
n1 = int(input("Enter first number: ")) #7
n2 = int(input("Enter Second number: ")) #5

def result():
    print(f'{x} is larger no. where as {y} is smaller.')
    

if n1>=n2:
    if n1>n2:
        x = n1 
        y = n2 
        result()
    else:
        print("Both number are same.")
else:
    x = n2
    y = n1
    result()
#Output: 7 is larger no. where as 5 is smaller
