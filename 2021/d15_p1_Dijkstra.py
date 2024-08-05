# Dijkstra's algorithm

import heapq

# Read the cave map
with open('2021_d15_input.txt', 'r') as file:
    lines = file.readlines()

# print(lines[1])
print(len(lines)) 

# Create a grid/matrix 100 * 100 of risk levels
# It strips any leading or trailing whitespace characters from each line and converts the characters into integers
risk = [list(map(int, line.strip())) for line in lines]
print(len(risk[0]) * len(risk) )

# Initialize a priority queue to explore paths
paths = [(0,0,0)]

# Initialize a 2D array to keep track of visited positions
vis = [[0] * len(row) for row in risk]

# Define the dimensions of the cave 100 * 100
rows = len(risk) 
cols = len(risk[0])



while True:
    try:
        rf, x, y = heapq.heappop(paths)
    except IndexError:
        print("Error: No more paths to explore. Algorithm terminated.")
        break

    if vis[x][y]:
        continue

    if (x, y) == (rows - 1, cols - 1):
        print("Lowest total risk of any path:", rf)
        break

    vis[x][y] = 1

    # Explore adjacent positions
    for nx, ny in [(x-1,y) , (x+1,y) , (x,y-1) , (x,y+1)]:
        if not (0<=nx<rows and 0<=ny<cols):
            continue
        if vis[nx][ny]:
            continue
        heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))
