
import itertools
import math
rows = [line.strip() for line in open("input.txt").readlines()]
ROWS, COLS = len(rows) - 1, len(rows[0]) - 1

table = {}
for r in range(ROWS):
    for c in range(COLS):
        signal = rows[r][c]
        if signal != ".":
            if signal not in table:
                table[signal] = []
            table[signal].append((r, c))

superSets = {}
for char, coords in table.items():
    superSets[char] = list(itertools.permutations(coords, 2))
    

def findDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xx = (x2 - x1) 
    yy = (y2 - y1) 
    return (xx, yy)

anti = set()
wrong = set()
for char, ss in superSets.items():
    for pairs in ss:
        p1, p2 = pairs
        distance = findDistance(p1, p2)
        antinode1 = tuple(x - y for x, y in zip(p1, distance))
        antinode2 = tuple(x + y for x, y in zip(p2, distance))
        x1, y1 = antinode1
        x2, y2 = antinode2
        if (x1 < 0 or x1 > ROWS or y1 < 0 or y1 > COLS): 
            print("INVALID NODE ", (x1, y1))
            wrong.add(antinode1)
            antinode1 = None
        if (x2 < 0 or x2 > ROWS or y2 < 0 or y2 > COLS): 
            print("INVALID NODE ", (x2, y2))
            wrong.add(antinode2)
            antinode2 = None

        if antinode1: anti.add(antinode1)
        if antinode2: anti.add(antinode2)
print(len(anti))




antinodes = set()
grid = []
nodes = {}

for line in open("input.txt"):
    if line.strip() == "": continue
    grid.append(line.strip())

N = len(grid)
M = len(grid[0])
for i in range(N):
    for j in range(M):
        if grid[i][j] != ".":
            if grid[i][j] in nodes:
                nodes[grid[i][j]].append((i,j))
            else:
                nodes[grid[i][j]] = [(i,j)]

def antinode(pr1, pr2):
    x1, y1 = pr1
    x2, y2 = pr2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    if newx >= 0 and newx < N and newy >= 0 and newy < M:
        antinodes.add((newx,newy))
                
for k in nodes:
    node_list = nodes[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            node1 = node_list[i]
            node2 = node_list[j]
            antinode(node1, node2)
            antinode(node2, node1)

print(len(antinodes))

print(antinodes - anti)


