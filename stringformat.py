#format() method allows you to format selected parts of a string
#add placeholders for the text to be formatted using {}
price = 50
txt = "The price is {} dollars"
print(txt.format(price)) #The price is 50 dollars

#multiple placeholders can be used
#parameters inside curly braces control formatting - .2f (two decimals)
order = "I want {} pieces of item number {} for {:.2f}"
print(order.format(3, 20, 25))

#placeholders can be indexed
order = "I want {0} pieces of item number {1} for {2:.2f}"
print(order.format(3, 20, 25))

#same index number can be repeated
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(25, "John"))

#named indexes can be used
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))