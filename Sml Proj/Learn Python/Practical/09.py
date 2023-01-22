#Program 9
num = int(input("Enter a number: ")) #23

# prime numbers are greater than 1
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
# if the entered number is less than or equal to 1
# it is not a prime number
else:
   print(num,"is not a prime number")
# Output: 23 is a prime number.
