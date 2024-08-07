
sum = 0

for line in open('input.txt', 'r'):
    digits = [char for char in line if char.isdigit()]
    sum += int(digits[0] + digits[-1])

print(sum)
