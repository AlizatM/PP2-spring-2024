import re
with open("row.txt", "r", encoding="utf-8") as s:
    text = s.read()
    matches = re.sub("\s",":", text)

print(matches)
