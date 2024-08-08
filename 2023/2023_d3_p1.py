grid = open('input.txt').read().splitlines()

digits = set()

for r, row in enumerate(grid): # for each row
    for c, ch in enumerate(row): # for each character
        if ch.isdigit() or ch == ".": # find symbols only
            continue
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2): #  8 flanking positions
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                while dc > 0 and grid[dr][dc - 1].isdigit(): # move to start of digit
                    dc -= 1
                digits.add((dr, dc)) # add start positions of each digit X, Y

ns = []

for r, c in digits:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit(): # start at the start, move along the number
        s += grid[r][c]
        c += 1
    ns.append(int(s)) # add it

print(sum(ns))
