import re

with open("input.txt", "r") as file:
    input_text = file.read()

clean_input = re.sub(r"don't\(\)[\w\W]*?do\(\)", "", input_text)
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", clean_input)
res = sum(int(x) * int(y) for x, y in matches)

print(res)
