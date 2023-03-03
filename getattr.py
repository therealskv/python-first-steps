#getattr() returns the value of the named attribute of an object
#if not found, it returns the default value provided to the function

#syntax - getattr(object, attr_name, [default_value])
#default_value is optional and is returned if the attribute is not found
class Student:
    marks = 100
    name = 'John'

person = Student()

name = getattr(person, 'name')
print(name)

try:
    age = getattr(person, 'age') #returns error
except Exception as e:
    print(e)

age = getattr(person, 'age', 15) #returns default value
print(age)