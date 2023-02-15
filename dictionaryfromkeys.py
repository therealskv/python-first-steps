#fromkeys() method creates a dictionary from the given sequence of keys and values
# keys for the dictionary
alphabets = {'a', 'b', 'c'}

# value for the dictionary
number = 1

# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)

print(dictionary)

# Output: {'a': 1, 'c': 1, 'b': 1}

nums = {'1', '2', '3'}

#if no value is provided, all values will be set to None
dictionary2 = dict.fromkeys(nums)

print(dictionary2)
#{'2': None, '1': None, '3': None}