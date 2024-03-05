import re
with open("row.txt", "r", encoding="utf-8") as s:
    text = s.read()
    snake = re.split(r"_", text)

s = snake[0]  
for i in range(1, len(snake)):
    s += snake[i].capitalize()  

print(s)