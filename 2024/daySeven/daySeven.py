
equations = {int(e[0]):[int(i) for i in e[1].strip().split()] for e in list(map(lambda x: x.rstrip().split(":"),open("input.txt").readlines()))}
def valid(match, res, arr, n, i):
    if n == 0:
        if res ==  match: return True
        else: return False
    val = arr[i]
    return valid(match, res + val, arr, n - 1, i + 1) or valid(match, res * val, arr, n - 1, i + 1) or valid(match, int(str(res) + str(val)), arr, n - 1, i + 1)

res = []
total = 0
for m, n in equations.items():
    if valid(m, 0, n, len(n), 0):
        res.append((m, n))
        total += m
print(total)
    
