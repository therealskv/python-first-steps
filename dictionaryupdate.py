#the update() method updates the dictionary with the elements
#from another dictionary object or from an iterable of key/value pairs

one = {1: 'one', 2: 'two'}
two = {3: 'three'}

one.update(two)

print(one) #{1: 'one', 2: 'two', 3: 'three'}

#when tuple is passed as a parameter

d1 = {'a': 1}
d1.update([('b', 2), ('c', 3)])

print(d1) #{'a': 1, 'b': 2, 'c': 3}
