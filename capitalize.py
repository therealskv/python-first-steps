def capitalize(s):
    result = ""
    prev = ""
    for i in range(len(s)):
        if prev == "" or prev == " ":
            result += s[i].upper()
        else:
            result += s[i]
        prev = s[i]
    return result

txt = input("Enter a string: ")
print(capitalize(txt))