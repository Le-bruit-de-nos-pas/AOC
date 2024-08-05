

a = [0]

with open("inputs/2022_d1_p1_input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            a.append(0)
            continue
        
        if not a:
            a.append(0)
        
        a[-1] += int(line.strip())

print(max(a))
