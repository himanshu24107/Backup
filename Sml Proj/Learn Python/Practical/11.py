#Program 11
n = int(input("Enter the number of terms: "))

# initializing first two terms
first = 0
second = 1

print("<--Fibonacci sequence-->")
for i in range(n):
    if i <= 1:
        next = i
    else:
        next = first + second
        first = second
        second = next
    print(next)
