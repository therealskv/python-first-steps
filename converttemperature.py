def convert_temperature(n, unit):
    if unit == "F":
        return (float(num) * 1.8) + 32
    else:
        return (num - 32) / 1.8

num = input("Enter number to convert: ")
unit = input("Convert to unit (F/C): ")
print(convert_temperature(int(num), unit))