#uses match and case keywords introduced in Python 3.10
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
     
    match choice:
        case "1":
            print(add(num1, num2))
        case "2":
            print(subtract(num1, num2))
        case _:
            print("Invalid input")
    
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break