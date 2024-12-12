grid = list(map(list, open("input.txt").read().splitlines()))

ROWS, COLS = len(grid), len(grid[0])
START = (0, 0)

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == "^":
            START = (i, j)
            break
print(START)

r, c = START
def loops(grid, r, c):
    dr, dc = -1, 0
    VISITED = set()
    while True:
        VISITED.add((r, c, dr, dc))
        if (r + dr < 0) or (r + dr >= ROWS) or (c + dc < 0) or (c + dc >= COLS):
            return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in VISITED:
            return True

count = 0
for rr in range(ROWS):
    for cc in range(COLS):
        if grid[rr][cc] != ".": continue
        grid[rr][cc] = "#"
        if loops(grid, r, c):
            count += 1
        grid[rr][cc] = "."
print(count)



            

            

                



        
    