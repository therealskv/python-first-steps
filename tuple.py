#tuple is a collection which is ordered and unchangeable
#tuples are unchangeable - items cannot be added or removed
#after the tuple has been created
#tuple items can be of any data type
new_tuple = ("apple", "bag", "cat")
print(new_tuple)
#items are indexed and ordered
print(new_tuple[0])

#length of a tuple
print(len(new_tuple))

#tuple with one item - add a comma after the item
#otherwise Python will not recognize it as a tuple

#this is considered just a string
new_tuple2 = ("apple")
print(new_tuple2)

new_tuple2 = ("apple",)
print(new_tuple2)
print(len(new_tuple2))

#tuple constructor
new_tuple3 = tuple((1, 2, 3))