#sytax - filter(function, iterable)
#filter() function extracts elements from an iterable - list, set, tuple etc.
#for which the function returns true
#it returns an iterator

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_numbers(number):
    return True if number % 2 == 0 else False

filtered_numbers = filter(filter_numbers, numbers)

even_numbers = list(filtered_numbers)
print(even_numbers)

#filter with lambda
filtered_numbers2 = filter(lambda num: (num % 2 != 0), numbers)

odd_numbers = list(filtered_numbers2)
print(odd_numbers)

#when None is used as the first argument, all elements that are truthy values
#i.e. gives True if converted to boolean, are extracted
random_list = [1, 'a', 0, False, True, '0']
filtered_iterator = filter(None, random_list)
filtered_list = list(filtered_iterator)
print(filtered_list)
