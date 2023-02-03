import re

str = "The Brown Fox In Town"
result = re.findall("[A-Z]own", str)
print(result) #['Town]

result = re.findall("[a-zA-Z]own", str)
print(result) #['rown', 'Town]