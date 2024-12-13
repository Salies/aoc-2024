file = open('data/1.txt', 'r')
lines = file.readlines()

left = []

n_counts = {}

for line in lines:
    ln, rn = line.strip().split('   ')
    ln, rn = int(ln), int(rn)

    if rn not in n_counts:
        n_counts[rn] = 0

    if ln not in n_counts:
        n_counts[ln] = 0
    
    n_counts[rn] += 1
    left.append(ln)

sim = 0
for i in range(len(left)):
    sim += left[i] * n_counts[left[i]]

print(sim)


