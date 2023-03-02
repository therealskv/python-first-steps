#delattr() deletes an attribute from the object
#syntax - delattr(object, attr_name)

class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()

print('x =', point1.x)
print('y =', point1.y)
print('z =', point1.z)

delattr(Coordinate, 'z')

# print('z =', point1.z) #raises error

#you can also delete an attribute using the del operator
del Coordinate.y


