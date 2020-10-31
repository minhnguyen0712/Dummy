# palindromic for strings
# Input: a string
# Output: true if given string is palindromic, false otherwise


def palindromic(s):
    if type(s) is not str:
        return False
    return s == s[::-1]


print(palindromic("abcdcba"))
print(palindromic("abca"))
print(palindromic(1))
