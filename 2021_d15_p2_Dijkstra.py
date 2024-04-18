# Dijkstra's algorithm

import heapq

# Read the cave map from input_2.txt
with open('inputs/2021_d15_input.txt', 'r') as file:
    lines = file.readlines()

# Create a grid of risk levels
# It strips any leading or trailing whitespace characters from each line and converts the characters into integers
_risk  = [list(map(int, line.strip())) for line in lines]

# Takes an integer x, subtracts 1 from it, takes the modulus 9, and adds 1 to the result.
# This operation ensures that if x is 9, it wraps back to 1, otherwise it remains the same
def wrap(x):
    return (x - 1) % 9 + 1

# expands the grid of risk levels to cover a 5x5 area
risk = [[0] * len(row) * 5 for row in _risk * 5]

r = len(_risk)
c = len(_risk[0])

# calculates and assigns the wrapped risk levels to each cell in the expanded grid
for i in range(len(risk)):
    for j in range(len(risk[i])):
        risk[i][j] = wrap(_risk[i % r][j % c] + i // r + j // c)


paths = [(0, 0, 0)]

vis = [[0] * len(row) for row in risk]

# repeatedly pops the top item from the priority queue paths
# checks if the position has been visited before, checks if the destination has been reached, marks the current position as visited
# explores adjacent positions, the priority queue ensures that positions with lower cumulative risk are explored first

while True:
    rf, x, y = heapq.heappop(paths)
    if vis[x][y]: continue
    if (x, y) == (len(risk) - 1, len(risk[x]) - 1):
        print(rf)
        exit(0)
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(risk) > nx >= 0 <= ny < len(risk[0]): continue
        if vis[nx][ny]: continue
        heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))