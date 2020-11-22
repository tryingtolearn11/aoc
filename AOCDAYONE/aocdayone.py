

def readInput(f): # Find Pos of the 1st Character that leads to Floor -1
    s = f.readlines() 
    level = 0
    counter = 0
    for line in s:
        for c in line:
            print("level : ", level)
            counter+=1
            if c =='(':
                level+=1
            elif c ==')':
                level-=1

            if level == -1: # Arrived at the Basement
                x = line.find(c)
                print("x : ", x)
                break
    print(" Position ", counter)
    print(" Character ", c)
    print("level ", level)


print(readInput(f=open("aocdayoneinput.txt", "r")))




