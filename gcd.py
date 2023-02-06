#highest common factor or greatest common divisor
#is the largest positive integer that perfectly
#divides given two numbers
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    
    return hcf

num1 = 54
num2 = 24
print("The HCF is", compute_hcf(num1, num2))