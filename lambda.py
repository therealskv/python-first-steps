#a lambda is a special type of function
#without a name
#syntax - lambda <arguments> : <expression>
greet = lambda : print('Hello World!')
greet()

#with argument
greet_user = lambda name : print('Hello', name, '!')
greet_user('Joe')

#with default argument value
greet_user = lambda name='Test' : print('Hello', name, '!')
greet_user()

#with multiple arguments
greet_user = lambda name, greeting='Hello' : print(greeting, name, '!')
greet_user('Joe', 'Good Morning')
greet_user('Joe')