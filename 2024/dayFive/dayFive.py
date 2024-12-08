import itertools

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



def correct(wrongUpdates):
    w = []
    c = []
    for u in wrongUpdates:
        perms = list(itertools.permutations(u))
        for perm in perms:
            stack = []
            for i in perm:
                stack.append(i)
                if i in orderRules.keys() and any([s for s in stack if s in orderRules[i]]):
                    w.append(perm)
                    break
        c.append([l for l in perms if l not in w]) 
    return c
ans = []
for i in correct(wrongUpdates):
    for j in i:
        ans.append(list(j))

for w,c in zip(wrongUpdates, ans):
    print(f"Wrong : {w}, Corrected : {c}")
print(sum([int(m[len(m) // 2]) for m in ans]))

