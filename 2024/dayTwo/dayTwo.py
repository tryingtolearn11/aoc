

def safe(levels):
    differences = [x - y for x, y in zip(levels, levels[1:])]
    return all(-1 >= diff >= -3 for diff in differences) or all(1 <= diff <= 3 for diff in differences)


def p1():
    count = 0
    levels = []
    with open("input.txt", encoding="utf-8") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if safe(levels):
                count += 1
    return count
print(p1())


def p2():
    count = 0
    levels = []
    with open("input.txt", encoding="utf-8") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if any(safe(levels[:index] + levels[index + 1:]) for index in range(len(levels))):
                count += 1
    return count
print(p2())
