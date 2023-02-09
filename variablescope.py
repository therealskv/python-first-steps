#local variables are defined inside a function
#and have a local scope
#they cannot be accessed outside the function

def hello():
    message = 'Hello'
    print('Local variable', message)

hello()
#print(message) #throws error

#global variables are declared outside a function
#and have a global scope
#they can be accessed inside or outside a function
global_message = 'Good Morning'
print('Global variable', global_message)