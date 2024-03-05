import re

with open("row.txt", "r", encoding="utf-8") as s:
    text = s.read()

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

print(camel_to_snake(text))