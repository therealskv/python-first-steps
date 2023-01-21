#conver two lists into a dictionary
list1 = [1, 2 , 3]
list2 = ['A', 'B', 'C']

#using zip function
dict1 = dict(zip(list1, list2))
print(dict1)

#using list comprehension
dict2 = {key: value for key, value in zip(list1, list2)}
print(dict2)