#zip function takes zero or more iterables,
#aggregates them in a tuple, and returns it
#syntax - zip(*iterables)

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

result = zip(numbers, letters)
print(set(result)) #prints a set of tuples

#when no arguments is passed, returns an empty iterator
print(set(zip()))

#with only one argument, each tuple has only one element
print(set(zip([1, 2, 3])))

#with more than two arguments, each tuple has elements from all iterables
print(set(zip([1, 2], ['a', 'b'], ['A', 'B'])))

#element length is equal to length of the shortest iterable, other elements are ignored
print(set(zip([1, 2], ['a', 'b', 'c'])))

#* operator can be used to unzip the items
result = zip(numbers, letters)
result_list = list(result)
nums, ltrs = zip(*result_list)
print(nums)
print(ltrs)