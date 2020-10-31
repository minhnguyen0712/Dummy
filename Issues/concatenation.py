# Concatenation problem
# Input: two strings
# Output: concat of two strings
# Author: Minh Nguyen


def concat(s1, s2):
    return str(s1) + str(s2)


def concat1(string_list):
    return "".join(string_list)


print(concat("a", "b"))
print(concat1(["a", "b", "c"]))
