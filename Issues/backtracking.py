# Backtracking problems
# Input: order arrangements of possibilities
# Output: list contains of all possibilities
# Author: minhnguyen


def backtrack(order, letters_list):
    if(order == 1):
        return letters_list
    else:
        return [y + x for y in backtrack(1, letters_list) for x in backtrack(order - 1, letters_list)]


print(backtrack(1, ["a", "b", "c"]))
print(backtrack(2, ["a", "b", "c"]))
print(backtrack(3, ["a", "b", "c"]))
