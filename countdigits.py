def count_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

num = input("Enter a number: ")
print("Number of digits: " + str(count_digits(int(num))))