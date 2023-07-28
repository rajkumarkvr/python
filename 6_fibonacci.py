#Recursive functions

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Display Fibonacci series upto n-th term")
term=int(input("Enter the term for series: "))
print("The fibonacci series are: ")
for i in range(term):
    print(fibonacci(i),end=" ")
