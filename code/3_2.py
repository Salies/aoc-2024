import re

file = open("data/3.txt", "r")
lines = file.readlines()

r = "((mul)\(([0-9]+,[0-9]+)\))|(do\(\))|(don't\(\))"

sum = 0
mul_enabled = True
for line in lines:
    matches = re.findall(r, line.strip())
    
    for m in matches:
        if m[1] == "mul" and mul_enabled:
            a, b = m[2].split(',')
            a, b = int(a), int(b)
            sum += a * b
            continue

        if m[3] == "do()":
            mul_enabled = True
            continue

        if m[4] == "don't()":
            mul_enabled = False

print(sum)