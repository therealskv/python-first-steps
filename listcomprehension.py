#syntax - [<expression> for <item> in <list>]
word_letters = [letter for letter in 'hello']
print(word_letters)

#list comprehension with condition
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

#if else
odd_even = ['Even' if x % 2 == 0 else 'Odd' for x in range(20)]
print(odd_even)