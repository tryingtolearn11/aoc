import collections

l, r = [], []
with open("input.txt", encoding="utf-8") as file:
    for line in file:
        aux = line.strip().split()
        l.append(int(aux[0]))
        r.append(int(aux[1]))
l.sort()
r.sort()

def p1():
    distance = sum(abs(i - j) for i, j in zip(l, r))
    return distance
print(p1())

def p2():
    tableR = collections.Counter(r)
    return sum( (left * tableR[left]) for left in l)
print(p2())

