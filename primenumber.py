def is_prime(n):
    if n <= 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(i, " * ", n//i, " = ", n)
                return False
        else:
            return True

num = input("Enter a number: ")
print(is_prime(int(num)))