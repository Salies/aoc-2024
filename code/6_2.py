import numpy as np
from tqdm import tqdm

f = open("data/6.txt", "r")
inp = f.read().splitlines()
f.close()

grid = np.zeros((len(inp), len(inp[0])), dtype=int)

startpos = None
for idx, line in enumerate(inp):
    # find the indexes of all "#" in the line
    hash_indexes = [i for i, c in enumerate(line) if c == "#"]
    # find the index of "^" in the line
    caret_index = line.find("^")
    grid[idx, hash_indexes] = 2
    if caret_index != -1:
        startpos = (idx, caret_index)
        grid[idx, caret_index] = 1

og_grid = grid.copy()

candidates = np.argwhere(grid == 0)

blowupcount = 0
for c in tqdm(candidates):
    grid = og_grid.copy()
    dir = 45
    x, y = startpos
    lastmove = None
    movecount = 0

    grid[c[0], c[1]] = 2

    while movecount < 1e5:
        movecount += 1
        grid[x, y] = 1
        lastmove = (x, y)
        match dir:
            # move right
            case 0:
                y += 1 
            # move up
            case 45:
                x -= 1
            # move left
            case 90:
                y -= 1
            # move down
            case 135:
                x += 1

        # check for bounds
        if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[1]:
            break
        
        if grid[x, y] == 2:
            x,y = lastmove

            if dir == 0:
                dir = 135
                continue
            dir -= 45

    grid[grid == 2] = 0

    if movecount == 1e5:
        blowupcount += 1

print(blowupcount)