#the max function returns the largest item in an iterable
#it an also be used to find the largest item 
#between two or more parameters
#syntax1 - max(iterable, *iterables, key, default)
nums = [9, 7, 10, 6, 5]
max_number = max(nums)
print(max_number)

#strings are ordered alphabetically, and returns last one
words = ['Van', 'Cat', 'F', 'Good']
max_word = max(words)
print(max_word)

#for a dictionary returns the item with largest key
dict1 = {1: 'A', 9: 'Zoom', 99: 'Ball'}
print(max(dict1))

#uses the key param to compute the max
#below it uses the value of each key 
#and returns the key with max value
print(max(dict1, key = lambda x : dict1[x]))

#max without iterable
print(max(9, -9, 10, 150))
