import re

file = open("input.txt")
memory = file.read()

sample = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

total = 0

on = True
for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory):
    if match == "do()":
        on = True
    elif match == "don't()":
        on = False
    elif on:
        x, y  = map(int, match[4:-1].split(","))
        total += x * y

print(total)
