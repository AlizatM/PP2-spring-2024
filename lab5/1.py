import re
with open("row.txt", "r", encoding="utf-8") as s:
    text = s.read()
    matches = re.findall("а{1}б*", text)


print(matches)
