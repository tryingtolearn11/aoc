

# --- Day 6: Probably a Fire Hazard ---

import re




'''
def readInput(f):
    lines = f.read().splitlines()
    ex1 = 'turn on 0,0 through 999,999'
    ex2 = 'toggle 0,0 through 999,0'
    ex3 = 'turn off 499,499 through 500,500'
    #box = [ex1, ex2, ex3]
    box = [line for line in lines]

    light_grid = [[False for i in range(1000)] for j in range(1000)]
    count = 0
    for s in box:  
        print("s : ", s)
        # some python regex for numbers
        temp = re.findall(r'\d+', s)
        key = list(map(int, temp))
        print("coords : ", key)
        # Start and end positions
        x1, y1 = key[0], key[1]
        x2, y2 = key[2], key[3]
        #print(x1,",", y1," to ", x2, ",", y2)
        
        if "toggle" in s:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if light_grid[i][j] == False:
                        light_grid[i][j] = True
                    elif light_grid[i][j] == True:
                        light_grid[i][j] = False
        
        elif "on" in s:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    light_grid[i][j] = True

        elif "off" in s:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    light_grid[i][j] = False 
       

    # Find how many lights are on
    for i in range(len(light_grid)):
        for j in range(len(light_grid[i])):
            if light_grid[i][j] == True:
                count+=1
    print("count : ",count)

readInput(f= open("input.txt", "r"))
'''



# Part Two
# turn on -> +1 brightness
# turn on -> -1 brightness, minimum of 0
# toggle -> +2 brightness

def two(f):
    
    #ex1 = 'turn on 0,0 through 0,0'
   # ex2 = 'toggle 0,0 through 999, 999'
   # box = [ex1, ex2]
    ex4 = 'turn on 0,0 through 999,0'
    ex5 = 'toggle 0, 999 through 999, 999'
    ex6 = 'turn off 0,0 through 999, 0'
    lines = f.read().splitlines()
    box = [line for line in lines]
    light_grid = [[0 for i in range(1000)] for j in range(1000)]


    for s in box:  
        temp = re.findall(r'\d+', s)
        key = list(map(int, temp))
        x1, y1 = key[0], key[1]
        x2, y2 = key[2], key[3]
        
        if "toggle" in s:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    light_grid[i][j] += 2
        
        elif "on" in s:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    light_grid[i][j] += 1

        elif "off" in s:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if light_grid[i][j] > 0:
                        light_grid[i][j] -= 1
                    else:
                        light_grid[i][j] = 0

    # Total brightness
    total_brightness = 0
    for i in range(len(light_grid)):
        for j in range(len(light_grid[i])):
            total_brightness += light_grid[i][j]
    print("total_brightness :", total_brightness)



two(f= open("input.txt", "r"))




























