sum = 0

for line in open('input.txt', 'r'):
  digits = [char for char in line if char.isdigit()] # extract individual digits on each line
  sum += int(digits[0] + digits[-1]) # create double digit number consisting of first and last digits observed in line, add to sum
print(sum)
