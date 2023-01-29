#locals() method returns a dictionary with all the local
#variables and symbols for the current program

print(locals())

a = 10

print(locals())

#variable value can be changed using the locals() method
locals()['a'] = 100

print(locals())
print(a) #100