file = open("data/4.txt", "r")
lines = file.readlines()

grid = [list(line) for line in lines]

word = "XMAS"

# generic word search puzzle solving algorithm
# https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
# (lmao geeksforgeeks actually worked for once)

M, N = len(grid), len(grid[0])
L = len(word)
dirs = [
    (-1, 0), # N,
    (-1, 1), # NE,
    (0, 1), # E,
    (1, 1), # SE,
    (1, 0), # S,
    (1, -1), # SW,
    (0, -1), # W,
    (-1, -1) # NW
]

n_occurrences = 0
for i in range(M):
    for j in range(N):
        # if it starts with the first letter of the word
        if grid[i][j] == word[0]:
            # search in all directions
            for d in range(8):
                n_occurrences += 1
                for k in range(1, L):
                    nx, ny = i + k * dirs[d][0], j + k * dirs[d][1]
                    if nx < 0 or ny < 0 or nx >= M or ny >= N or grid[nx][ny] != word[k]:
                        n_occurrences -= 1
                        break

print(n_occurrences)