
equations = {int(e[0]):[int(i) for i in e[1].strip().split()] for e in list(map(lambda x: x.rstrip().split(":"),open("input.txt").readlines()))}
def valid(match, res, arr, n, i):
    if n == 0:
        if res ==  match: return True
        else: return False
    return valid(match, res + arr[i], arr, n - 1, i + 1) or valid(match, res * arr[i], arr, n - 1, i + 1) or valid(match, int(str(res) + str(arr[i])), arr, n - 1, i + 1)
print(sum([m for m, n in equations.items() if valid(m, 0, n, len(n), 0)]))