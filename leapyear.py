def is_leap_year(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

year = input("Enter the year: ")
print("The year " + year + " is " + ("a" if is_leap_year(int(year)) else "not a" )+ " leap year!")