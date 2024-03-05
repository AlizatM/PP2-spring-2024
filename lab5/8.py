import re
with open("row.txt", "r", encoding="utf-8") as s:
    text = s.read()
    x = re.split("[A-Z]", text)

print(x)