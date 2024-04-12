import re
with open("row.txt", "r", encoding = "utf-8") as s:
    file = s.read()
    x = re.findall("[a-z]+_+[a-z]+",file)
    print(x)
