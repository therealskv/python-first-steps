#map function applies a given function to each element of an iterable
#and returns an iterator containing the results
#syntax - map(function, iterable, ..)
#more than one iterable can be passed as argument

def square(n):
    return n*n

numbers = (1, 2, 3)
squared_numbers = map(square, numbers)
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)

#using lambda
cubed_numbers = map(lambda n: n*n*n, numbers)
print(list(cubed_numbers))

#passing multiple iterators
sum_of_numbers = map(lambda n1, n2: n1+n2, numbers, squared_numbers_list)
print(list(sum_of_numbers))