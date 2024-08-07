import re

sum = 0
string_list = "one two three four five six seven eight nine".split()
# "|".join(n) + "|\\d"     -> This would find the first time a number appears and jump to the end
pattern = "(?=(" + "|".join(n) + "|\\d))" # -> This starts matching again after every other character  (?=(...))

def literal_to_digit(x):
    if x in string_list:
        return str(string_list.index(x) + 1) # convert literal number from list to exact digit 1 to 9
    return x


for line in open('input.txt', 'r'):
  digits = [*map(literal_to_digit, re.findall(pattern, line))]
  sum += int(digits[0] + digits[-1])

print(sum)
