def is_palindrome(str):
    _str = str.casefold()
    rev_str = reversed(_str)

    if list(str) == list(rev_str):
        return True
    else:
        return False

str = input("Enter a word to check if it is a palindrome: ")
print(str, "is not" if is_palindrome(str) == False else "is", "a Palindrome!")