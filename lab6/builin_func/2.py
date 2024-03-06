def upper_lower(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    return upper, lower

string = "Hello World"
upper, lower = upper_lower(string)
print(upper)
print(lower)
