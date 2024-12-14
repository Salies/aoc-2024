import numpy as np

file = open("data/4.txt", "r")
lines = file.readlines()

grid = [list(line) for line in lines]

M = len(grid)
N = len(grid[0])

word = 'MAS'
count = 0
for i in range(1, M - 1):
    for j in range(1, N - 1):
        if grid[i][j] != 'A':
            continue
        # get 3x3 neighborhood
        neighborhood = [
            [grid[i + k][j + l] for l in range(-1, 2)] for k in range(-1, 2)
        ]

        neighborhood = np.array(neighborhood)

        # get diagonal elements
        diag1 = ''.join(neighborhood.diagonal())
        diag2 = ''.join(neighborhood[::-1].diagonal())

        if((diag1 != word and diag1 != word[::-1]) or (diag2 != word and diag2 != word[::-1])):
            continue

        count += 1

print(count)