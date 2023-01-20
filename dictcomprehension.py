#dictionaries allow to store data as key/value pairs
students = {'John': 15, 'Ram': 19, 'Jay': 18, 'Vin': 16}

#using comprehension code can be shortened
squares = {num: num*num for num in range(1, 11)}
print(squares)

weights_in_kg = {'rice': 5, 'oats': 2, 'wheat': 3, 'pulses': 4}
weights_in_lb = {item: weight*2.2 for (item, weight) in weights_in_kg.items()}
print(weights_in_lb)

#with condition
weights_in_lb = {item: weight*2.2 for (item, weight) in weights_in_kg.items() if weight % 2 == 0}
print(weights_in_lb)

#with multiple conditions
weights_in_lb = {item: weight*2.2 for (item, weight) in weights_in_kg.items() if weight % 2 == 0 and weight >= 4}
print(weights_in_lb)
