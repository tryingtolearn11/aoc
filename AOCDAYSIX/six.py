

# --- Day 6: Probably a Fire Hazard ---

import re





def readInput(f):
    lines = f.read().splitlines()
    box = [sentence for sentence in lines]
    for s in box:  
        # some python regex
        temp = re.findall(r'\d+', s)
        key = list(map(int, temp))
        # Start and end positions
        x1, y1 = key[0], key[1]
        x2, y2 = key[2], key[3]
        print(x1,",", y1," to ", x2, ",", y2)
        count = 0
        if "on" in s:
            # Test count for now
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    count+=1
            print (count)

readInput(f= open("input.txt", "r"))
