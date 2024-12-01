

def wrappingPaper(f):
    s = f.read().splitlines()
    b = []
    for k in s:
        a = []
        a = k.split('x')
        b.append(a)    
    print(b)
    print("len of b : ", len(b))
    
    sum_of_surfaceA = 0
    totalRibbon = 0
    # Sort Strings to Integers
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = int(b[i][j])
    

    # Compute Areas
    for i in range(len(b)):
        b[i].sort()
        print("dimensions : ", b[i])

        smallArea = b[i][0]*b[i][1]
        print("Small Area : ", smallArea)

        surfaceArea = 2*b[i][0]*b[i][1]+2*b[i][1]*b[i][2]+2*b[i][2]*b[i][0]
        print("Surface Area : ", surfaceArea)
        print()
        totalArea = surfaceArea + smallArea
        sum_of_surfaceA +=totalArea

        # Part Two : Ribbons
        
        shortest_perimeter = b[i][0]*2+b[i][1]*2
        print("Shortest Perimeter : ", shortest_perimeter)
        bowRibbon = b[i][0]*b[i][1]*b[i][2]
        print("Bow Ribbon : ", bowRibbon)
        ribbonNeeded = shortest_perimeter + bowRibbon
        totalRibbon += ribbonNeeded
        print("TOTAL RIBBON : ", totalRibbon)


    print("Wrapping paper need : ", sum_of_surfaceA)



wrappingPaper(f=open("inputfile.txt","r"))





















































