sum = 0

with open('input.txt', 'r') as file:
  for idx, line in enumerate(file):
    groups = line.strip().split(": ")[1].split("; ") # remove newline, get groups in game as list
    game_lkt = {"red": 0, "green": 0, "blue": 0} # max per game/line
    for group in groups:
        group_lookup = {"red": 0, "green": 0, "blue": 0} # max per group in game/line
        for cube in group.split(", "):
            a, b = cube.split()
            group_lookup[b] = int(a) # add number to group
        for colour in game_lkt:
            game_lkt[colour] = max(game_lkt[colour], group_lookup[colour]) # pick max colour current group vs other groups in line
    sum += game_lkt["red"] * game_lkt["green"] * game_lkt["blue"]

print(sum)
