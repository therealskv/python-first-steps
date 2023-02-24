#the type() function either returns the type of the object
#or returns a new type object based on the arguments

#syntax1 - type(object)
#returns - the type of the object

numbers = [1, 2]
print(type(numbers))

class Foo:
    a = 0

foo = Foo()
print(type(foo))

#syntax 2 - type(class_name, bases, dict)