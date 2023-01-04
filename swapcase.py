def swap_case(txt):
    result = ""
    for c in txt:
        if c.islower():
            result += c.upper()
        elif c.isupper():
            result += c.lower()
        else:
            result += c
    
    return result

txt = input("Enter a string: ")
print(swap_case(txt))