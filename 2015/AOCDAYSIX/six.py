

# --- Day 6: Probably a Fire Hazard ---

import re
# Part One
def p1(f):
    box = [line for line in f.read().splitlines()]
    light_grid = [[False for i in range(1000)] for j in range(1000)]
    count = 0

    for s in box:  
        temp = re.findall(r'\d+', s)
        key = list(map(int, temp))
        # Start and end positions
        x1, y1, x2, y2 = key[0], key[1], key[2], key[3]

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):

                if "on" in s:
                    light_grid[i][j] = True

                elif "off" in s:
                    light_grid[i][j] = False 


                else:
                    if light_grid[i][j]:
                        light_grid[i][j] = False
                    else:
                        light_grid[i][j] = True
        

    # Find how many lights are on
    for i in range(len(light_grid)):
        for j in range(len(light_grid[i])):
            if light_grid[i][j] == True:
                count+=1
    print("count : ",count)

p1(f= open("input.txt", "r"))

# Part Two
# turn on -> +1 brightness
# turn on -> -1 brightness, minimum of 0
# toggle -> +2 brightness


def two(f):
    
    box = [line for line in f.read().splitlines()]
    light_grid = [[0 for i in range(1000)] for j in range(1000)]


    for s in box:  
        temp = re.findall(r'\d+', s)
        key = list(map(int, temp))
        x1, y1, x2, y2 = key[0], key[1], key[2], key[3]
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):

                if "on" in s:
                    light_grid[i][j] +=1

                elif "off" in s:
                    if light_grid[i][j] > 0:
                        light_grid[i][j] -= 1
                
                else:
                    light_grid[i][j] += 2

    # Total brightness
    total_brightness = 0
    for i in range(len(light_grid)):
        for j in range(len(light_grid[i])):
            total_brightness += light_grid[i][j]
    print("total_brightness :", total_brightness)



two(f= open("input.txt", "r"))

