# Program 14
string = input("Enter a string: ").casefold()

if string == string[::-1]:
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")
