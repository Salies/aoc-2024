import bisect

file = open('data/1.txt', 'r')
lines = file.readlines()

left = []
right = []

for line in lines:
    ln, rn = line.strip().split('   ')
    ln, rn = int(ln), int(rn)
    bisect.insort(left, ln)
    bisect.insort(right, rn)

dist = 0
for i in range(len(left)):
    dist += abs(right[i] - left[i])

print(dist)