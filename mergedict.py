dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 4, 'y': 5, 'z': 6}

#using the | operator
print(dict1 | dict2)

#using the ** operator
print({**dict1, **dict2})

#copy dict
dict3 = dict1.copy()
print(dict3)

#add dict
dict3.update(dict2)
print(dict3)