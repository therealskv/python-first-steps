#the least common multiple of two numbers is 
#the smallest positive integer that is perfectly divisible
#by two given numbers
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    lcm = 0
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm

num1 = 54
num2 = 24
print("The least common multiple is", compute_lcm(num1, num2))