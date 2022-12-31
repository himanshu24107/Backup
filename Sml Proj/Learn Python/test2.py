string=input("enter a string:")
while True:
    if string[0]=='a':
        string=string[2:]
        # print(string) 
    elif string[-1]=='b':
        string=string[:2]
        # print(string)
    else:
        break
print(string)
