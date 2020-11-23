
# Day 3: Perfectly Spherical Houses in a Vacuum

def find_total_houses(f):
    instructions = f.read()
    houses = set()
    x, y = 0, 0
    start = (x, y)
    print(type(start))
    current = start 
    print(current, type(current))
    houses.add(start)

    for i in range(len(instructions)):
        print(instructions[i])
        if instructions[i] == '^': # Up
            y-=1
        elif instructions[i] == 'v': # Down
            y+=1
        elif instructions[i] == "<": # Left
            x-=1
        else:
            x+=1
        current = (x, y)
        print("Current Position : ", current)    
        houses.add(current)
    # print(houses)
    print("Houses visited : ", len(houses))     






find_total_houses(f=open("input.txt","r"))

