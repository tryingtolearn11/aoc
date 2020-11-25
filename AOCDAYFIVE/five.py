

# --- Day 5: Doesn't He Have Intern-Elves for This? ---


def find_nice_words(f):
    words = f.read().splitlines()
    nicewords = []
    example = "dvszwmarrgswjxmb"


    vowels = ("a", "e", "i", "o", "u")
    invalidsubstrings = (("ab"), ("cd"), ("pq"), ("xy"))
    
    for line in words:
        print("---------------------------------------")
        j = 0
        condition1, condition2, condition3 = False, False, False

        for i in line:
           if i in vowels:
               j+=1
           if j >= 3:
               print("condition 1 MET:", line)
               condition1=True
               break
           else:
               print("condition 1 Failed", line)

        for k in range(len(line)-1):
            if line[k] == line[k+1]:
                print("condition 2 MET:", line)
                condition2=True
                break
            else:
                print("condition 2 Failed", line)
        
        if any(x in line for x in invalidsubstrings):
            print("condition 3 Failed:", line)
            condition3=False
        else:
            condition3=True
            print("condition 3 Met", line)
        
        if condition1 and condition2 and condition3:
            nicewords.append(line)
            print("------ NICE WORD CONFIRMED----- ", line)
    print("nicewords ---------------- ")
    print(nicewords)
    return len(nicewords)

# print(find_nice_words(f=open("input.txt", "r")))



def find_nice_words_p2(f):


    box = f.read().splitlines()
    nicewords = []
    for textstring in box:
        con1, con2 = False, False
        i, j = 0, 1
        y = len(textstring)-1
        x = y-1
        while i < len(textstring) and j < y:
            while x > j and y > x:
                print("x, y : ", textstring[x], textstring[y])
                if textstring[i]==textstring[x] and textstring[j]==textstring[y]:
                    print("FOUND PAIR ")
                    print("i , j :", textstring[i],textstring[j])
                    print("x, y :", textstring[x], textstring[y])
                    print("-----------------------------")
                    con1 = True
                    break
                
                else:
                    x-=1
                    y-=1
                    print("i , j : ", textstring[i], textstring[j])

            if con1:
                break
            else:
                i+=1
                j+=1
                y = len(textstring)-1
                x = y-1
        print("i ", i, "  j ", j)
        print("x ", x, "y ", y)

        # Condition 2
        for k in range(len(textstring)-2):
            if textstring[k] == textstring[k+2]:
                con2 = True
        
        if con1 and con2:
            nicewords.append(textstring)
    print(nicewords)
    print("TOTAL NICE WORDS : ", len(nicewords))
   

print(find_nice_words_p2(f=open("input.txt","r")))


























