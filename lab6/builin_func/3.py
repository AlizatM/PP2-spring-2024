def is_palindrome(string):
    return string == string[::-1]

string = "radar"
if is_palindrome(string):
    print("Yes")
else:
    print("No")
