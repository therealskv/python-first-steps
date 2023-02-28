#ascii() method replaces a non-printable character
#with its corresponding ascii value and returns it

text = 'Pythön is interesting'
print(text)
print(ascii(text)) # replaces ö with its ascii value

#syntax - ascii(object)
#the parameter can be a list, set, tuple etc.

#ascii() with a list
list = ['Pythön', 'öñ', 5]
print(ascii(list))

#ascii() with a set
set = {'Π', 'Φ', 'η'}
print(ascii(set))

#ascii() with a tuple
tuple = ('ö', '√', '¶','Ð','ß' )
print(ascii(tuple))
