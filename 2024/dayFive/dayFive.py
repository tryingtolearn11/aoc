file = open("sample.txt")
rules, updates = [], []
for line in file:
    line = line.replace('\n', '')
    if not line:
        continue
    rules.append(line) if "|" in line else updates.append(line)

orderRules = {}
for s in rules:
    k, v = s.split("|")
    if k not in orderRules.keys():
        orderRules[k] = []
    orderRules[k].append(v)

updateOrder = []
for u in updates:
    updateOrder.append(u.split(","))

# Check if any of the past elements are in the curr's values
wrongUpdates = []
def validateUpdates(updateOrder):
    for update in updateOrder:
        stack = []
        for page in update:
            stack.append(page)
            if page in orderRules.keys() and any([s for s in stack if s in orderRules[page]]):
                wrongUpdates.append(update)
                break
    return [c for c in updateOrder if c not in wrongUpdates]
print(sum([int(m[len(m) // 2]) for m in validateUpdates(updateOrder)]))

# Not my code, needed help
def format_input(inp):
    pairs = set((n1,n2) for n1, n2 in [map(int, l.strip().split('|')) for l in inp if '|' in l])
    updates = [list(map(int, l.strip().split(','))) for l in inp if ',' in l]
    return pairs, updates


with open("input.txt", 'r') as file:
    inp = file.readlines()

pairs, updates = format_input(inp)
print(pairs, updates)

def correctUpdate(u):
    return sorted(u, key=lambda x: sum([(e, x) in pairs for e in u]))

def findIncorrect(updates):
    return [u for u in updates if u != correctUpdate(u)]
print(findIncorrect(updates))

print("P2: ", sum([u[len(u)//2] for u in map(correctUpdate, findIncorrect(updates))]))
