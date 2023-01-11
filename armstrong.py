#A n-digit positive integer is an Armstrong number if
#abcd....n = a^n + b^n + c^n + d^n + ... + n^n
def is_armstrong(num):
    order = len(num)
    num = int(num)
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    if sum == num:
        return True
    else:
        return False


num = input("Enter a number: ")
print(num + " is " + ("a" if (is_armstrong(num)) else "not a") + " Armstrong number!")