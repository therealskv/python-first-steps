def fibonacci(n):
    if(n == 0 or n == 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num = input("Enter a number: ")
for n in range(int(num)):
    print(fibonacci(n), end =" ")