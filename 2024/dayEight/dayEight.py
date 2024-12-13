
import itertools
import math
rows = [line.strip() for line in open("sample.txt").readlines()]
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
    xx = (x2 - x1) ** 2
    yy = (y2 - y1) ** 2
    return math.sqrt(xx + yy)

distances = {}
for char, ss in superSets.items():
    for pairs in ss:
        p1, p2 = pairs
        print(p1, p2, findDistance(p1, p2))
