file = open("input.txt")
data = file.read()
arr = []
row = ""
for line in data:
    if line.isalpha():
        row += line
    else:
        arr.append(row)
        row = ""
'''
arr = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]
'''

DIRECTIONS = [(0,1),(-1,0),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
def p1():
    s = 0  # Counter for occurrences of "XMAS"
    # Iterate over the grid
    for y in range(len(arr)):  # Rows
        for x in range(len(arr[0])):  # Columns
            for dy, dx in DIRECTIONS:
                # Check if the word "XMAS" fits in this direction
                if (
                    0 <= y + 3 * dy < len(arr) and
                    0 <= x + 3 * dx < len(arr[0])
                ):
                    # Match the pattern "XMAS"
                    if (
                        arr[y][x] == 'X' and
                        arr[y + dy][x + dx] == 'M' and
                        arr[y + 2 * dy][x + 2 * dx] == 'A' and
                        arr[y + 3 * dy][x + 3 * dx] == 'S'
                    ):
                        s += 1

    return s
print(f"Occurrences of 'XMAS': {p1()}")




TABLE = {"M", "S"}
# Find A, Search Diagonal for M and S
def p2():
    s = 0
    for r in range(1, len(arr) - 1):
        for c in range(1, len(arr[0]) - 1):
            if arr[r][c] == "A":
                if {arr[r - 1][c - 1], arr[r + 1][c + 1]} == TABLE and {arr[r - 1][c + 1], arr[r + 1][c - 1]} == TABLE:
                    s += 1
    return s  
print(f"Occurrences of 'MAS': {p2()}")