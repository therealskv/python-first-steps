#globals() method returns a dictionary with all 
#the global variables and symbols for the current program

print(globals())

b = 25

print(globals())

globals()['b'] = 50

print(globals())
print(b) #50