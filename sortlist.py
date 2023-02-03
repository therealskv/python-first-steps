#sorted() function returns a sorted list of the given iterable object
#syntax - sorted(iterable, key, reverse)
#key - a function that is used for sorting

arr = (99, 10, 50, 12, 0, 1)
sorted_arr = sorted(arr)
print(sorted_arr)

sorted_arr = sorted(arr, reverse=True)
print(sorted_arr)

sorted_arr = sorted(arr, key=lambda x: x*-1)
print(sorted_arr)