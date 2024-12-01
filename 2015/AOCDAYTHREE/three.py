
# Day 3: Perfectly Spherical Houses in a Vacuum

def find_total_houses_p1(f):
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






# find_total_houses_p1(f=open("input.txt","r"))

# ----------Part Two---------------------------

def find_total_houses_p2(f):
    instructions = f.read()
    houses = set()
    x, y = 0, 0
    a, b = x, y
    start = (x, y)
    # Set Santa's current Position to Start
    currentSanta = start
    # Set Robo-Santa's curr pos to start too
    currentRobo = start 
    houses.add(start)
    print("currentSanta : ", currentSanta)
    print("currentRobo ", currentRobo )
    

    for i in range(len(instructions)):
        print("i : ", i)
        print(instructions[i])
        if i % 2 == 0: # If Even Give Instructions to Santa
            if instructions[i] == '^': # Up
                y-=1
            elif instructions[i] == 'v': # Down
                y+=1
            elif instructions[i] == "<": # Left
                x-=1
            else:
                x+=1
            currentSanta = (x, y)
        else: # i is odd -> Give instructions to Robo-Santa
            if instructions[i] == '^': # Up
                b-=1
            elif instructions[i] == 'v': # Down
                b+=1
            elif instructions[i] == "<": # Left
                a-=1
            else:
                a+=1
            currentRobo = (a, b)

        print("Current Santa Position : ", currentSanta)    
        print("Current Robo- Position : ", currentRobo)
        houses.add(currentSanta)
        houses.add(currentRobo)
    # print(houses)
    print("Houses visited : ", len(houses))     






find_total_houses_p2(f=open("input.txt","r"))


