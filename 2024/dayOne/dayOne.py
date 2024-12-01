import collections
path = '/Users/damiensingh/aoc2024/dayOne/input.txt'
with open(path, encoding="utf-8") as f:
    data = f.read()
    
d = data.split("\n")
l, r = [], []
for line in d:
    aux = line.strip().split()
    if not aux: continue
    left, right = int(aux[0]), int(aux[1])
    l.append(left)
    r.append(right)
l.sort()
r.sort()

def p1():
    distance = 0
    for i, j in zip(l, r):
        distance += abs(i - j)
    return distance
print(p1())

def p2():
    sScore = 0
    tableL = collections.Counter(l)
    for n in r:
        if n in tableL:
            sScore += (n * tableL[n])
    return sScore


print(p2())

