#sum of n natural numbers = n*(n+1)/2
def sum_numbers(num):
    if(num < 0):
        return "Enter a positive number"
    else:
        return "Sum of " + str(num) + " number is " + str(num * (num + 1) / 2)

num = input("Enter a number: ")
print(sum_numbers(int(num)))