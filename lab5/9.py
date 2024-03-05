import re
with open("row.txt", "r", encoding="utf-8") as s:
    text = s.read()
def splitUp(s):
    words = re.findall(r"[A-Z][a-z]+", s)
    return " ".join(words)
print(splitUp(text))