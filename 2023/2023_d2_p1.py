sum = 0

with open('input.txt', 'r') as file:
  for idx, line in enumerate(file):
    groups = line.strip().split(": ")[1].split("; ") # remove newline, get groups in game as list
    for group in groups:
        lookup = {"red": 0, "green": 0, "blue": 0}
        for cube in group.split(", "):
            a, b = cube.split()
            lookup[b] = int(a) # see how many cubes og each colour
        if lookup["red"] > 12 or lookup["green"] > 13 or lookup["blue"] > 14:
            break
    else: # if it did not break, run this else statement
        sum += idx + 1

print(sum)
