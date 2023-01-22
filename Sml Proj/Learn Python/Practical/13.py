#Program 13
string = input("Enter a string: ")
lower = 0
upper = 0
other = 0

for i in string:
    if i.isalpha():
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    else:
        other += 1

print("Number of Lowercase characters:", lower)
print("Number of Uppercase characters:", upper)
print("Number of Other characters:", other)
