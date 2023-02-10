#closure is a nested function
#that allows us to access variables
#of the outer function even after the outer function is closed

#nested function
def greet(name):
    def display_name():
        print("Hello", name)
    display_name()

greet("John")

#a nested function can be returned from the outer function
def greet():
    name = 'John'

    return lambda: "Hi " + name

message = greet()

#nested function acts a closure that encloses the outer scope variable
#within its scope even after the outer function is executed
#hence it is able to access the variable name from the outer function
#even after the outer function call is complete
print(message())

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
print(times3(9))