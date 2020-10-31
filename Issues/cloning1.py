# Cloning problems
# Input: list, string,int
# Output: copies of them


def cloning(s):
    if type(s) is int:
        x = int(s)
        return x
    if type(s) is str:
        x = str(s)
        return x
    if type(s) is list:
        x = list(s)
        return x


a = [1, 2, 3]
x = ["1,", "2,", "3,"]
b = cloning(a)
y = cloning(x)
print(b, y)
