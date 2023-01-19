#a set is a collection of unique data
#the elements in a set can be of different types
#but the elements cannot be mutable  elements like lists, sets or dictionaries

#defining a set
ids = {1000, 5000, 6000, 9000}
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

#creating an empty set
temp_set = set()
print(type(temp_set))

#declaring using empty {} creates a dictionary
temp_dict = {}
print(type(temp_dict))

#add items to a set
ids.add(1000)

#remove item
ids.discard(9000)

#iterate over a set
for id in ids:
    print(id)

odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
#union operation returns elements from both sets
#using | operator or union() method
print('Union using | operator: ', odd | even)
print('Union using union()): ', odd.union(even))

#& operator or intersection() method returns common elements
print('Intersection using & operator: ', odd & even)
print('Intersection using intersection(): ', odd.intersection(even))

#difference between two sets
print('Difference using & operator: ', odd - even)
print('Difference using difference(): ', odd.difference(even))

#symmetric difference returns all elements except for the common elements
print('Symmetric difference using ^ operator: ', odd ^ even)
print('Symmetric difference using symmetric_difference(): ', odd.symmetric_difference(even))

#compare two methods
print("Both sets are ", "equal" if odd == even else "not equal")