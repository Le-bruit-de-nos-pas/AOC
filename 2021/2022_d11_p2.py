targets = []

with open('test.txt') as file:
  for monk in file.read().strip().split("\n\n"):
    lines = monk.splitlines()
    target = []
    target.append(list(map(int, lines[1].split(": ")[1].split(", "))))
    target.append(eval( "lambda old:" + lines[2].split("=")[1]))
    for line in lines[3:]:
      target.append(int(line.split()[-1]))
    targets.append(target)


counts = [0] * len(targets)


mod = 1
for target in targets:
  mod *= target[2]

for _ in range(10000):
  for index, target in enumerate(targets):
    for item in target[0]:
      item = target[1](item)
      item %= mod
      if item % target[2] == 0:
        targets[target[3]][0].append(item)
      else:
        targets[target[4]][0].append(item)
    counts[index] += len(target[0])
    target[0] = []

counts.sort()

print(counts[-1]*counts[-2])
