#the copy() method returns a copy of the dictionary
original = {1: "One", 2: "two"}
copy = original.copy()

print(original)
print(copy)

#any changes to the original doesn't impact the copy
original.clear()

print(original)
print(copy)