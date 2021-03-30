
# --- Day 7: Some Assembly Required ---

import functools

def solution(f):
    # create hash table to store wires
    circuit = {}
    data = [line for line in f.read().splitlines()]
    
    for i in data:
        # Circuit[right-hand side] = left-hand side
        circuit[i.split("->")[-1].strip()] = i.split("->")[0].strip()
    print(circuit)
    print("-----------------------------------------")
   
    # Recursive
    @functools.lru_cache()
    def get_value(key):
        try:
            return int(key)
        except ValueError:
            pass

        s = circuit[key].split(" ")

        if "NOT" in s:
            return ~get_value(s[1])
        if "AND" in s:
            return get_value(s[0]) & get_value(s[2])
        elif "OR" in s:
            return get_value(s[0]) | get_value(s[2])
        elif "LSHIFT" in s:
            return get_value(s[0]) << get_value(s[2])
        elif "RSHIFT" in s:
            return get_value(s[0]) >> get_value(s[2])
        else:
            return get_value(s[0])

    # Solution to p2 -Comment out circuit["b"] to get p1 solution
    #circuit["b"] = str(get_value("a"))
    get_value.cache_clear()
    print(get_value("a"))

solution(f=open("input.txt", "r"))




