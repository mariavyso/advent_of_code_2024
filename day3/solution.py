import re

with open("input.txt", "r") as file:
    input_text = file.read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_text)
res = sum(int(x) * int(y) for x, y in matches)

print(res)
