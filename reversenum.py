#uses recursion to reverse a number
def reverse_number_recursion(num, reversed_num=0):
    if num == 0:
        return reversed_num
    else:
        digit = num % 10
        reversed_num = reversed_num*10 + digit
        return reverse_number_recursion(num//10, reversed_num)

#using loop
def reverse_number_loop(num):
    reversed_num = 0;
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num*10 + digit
        num //= 10
    
    return reversed_num

#using slice
#syntax [start:stop:step]
#when step is set to -1, start point goes to end and stop to front
def reverse_number_slice(num):
    return str(num)[::-1]

num = input("Enter a number: ")
print('Reversed number using recursion is', reverse_number_recursion(int(num)))
print('Reversed number using loop is', reverse_number_loop(int(num)))
print('Reversed number using slicing is', reverse_number_slice(int(num)))