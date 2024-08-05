from copy import deepcopy as dp

m = []

def convert(x):
    if isinstance(x, int):
        return[x]
    return [convert(e) for e in x]

for line in open('inputs/2021_d18_input.txt', 'r'):
    m.append(convert(eval(line)))


def addright(x, v):
    if x is None: 
        return
    if len(x) == 1:
        x[0] += v
    else:
        addright(x[1], v)


def addleft(x, v):
    if x is None: 
        return
    if len(x) == 1:
        x[0] += v
    else:
        addleft(x[0], v)


def explode(x, l = None, r = None, d = 0):
    if len(x) == 1:
        return False
    if d >= 4 and len(x[0]) == len(x[1]) == 1:
        addright(l, x[0][0])
        addleft(r, x[1][0])
        x[:] = [0]
        return True
    return explode(x[0], l, x[1], d+1) or explode(x[1], x[0], r, d+1 )
    

def split(x):
    if len(x) == 1:
        if x[0] >=10:
            x[:] = [ [x[0] // 2 ] , [-(-x[0] // 2)]] # floor , ceill 
            return True
        else:
            return False
    else:
        return split(x[0]) or split(x[1])
    

def reduce(x):
    while explode(x) or split(x):
        pass


def mag(x):
    if len(x) == 1:
        return x[0]
    else:
        return 3*mag(x[0]) + 2*mag(x[1])

ms = -float("inf")

for i in range(len(m)):
    for j in range(len(m)):
        if i == j:
            continue
        k = dp([m[i] , m[j]])
        reduce(k)
        ms = max(ms, mag(k))


print(ms)