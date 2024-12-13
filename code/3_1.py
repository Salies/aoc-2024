import re

file = open("data/3.txt", "r")
lines = file.readlines()

r = "((mul)\(([0-9]+,[0-9]+)\))"

sum = 0

for line in lines:
    matches = re.findall(r, line.strip())

    for m in matches:
        a, b = m[2].split(',')
        a, b = int(a), int(b)
        sum += a * b

print(sum)