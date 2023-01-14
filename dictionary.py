dt = {'x': 1, 'y': 2, 'z': 3}

#using items
for key, value in dt.items():
    print(key, value)

#get value using key
for key in dt:
    print(key, dt[key])

#get all keys
for key in dt.keys():
    print(key)
#get all values
for value in dt.values():
    print(value)

