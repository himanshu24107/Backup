def add():
    a =input("Enter first no:")
    if a=="end":
        pass
    else:
        a = int(a)

    b = int(input("Enter second no:"))
    c=a+b
    print(c)
    add()
add()
