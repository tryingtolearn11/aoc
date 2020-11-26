

# --- Day 6: Probably a Fire Hazard ---


class Board:
    def __init__(self, light):
        self.board = []
        self.x = 50
        self.y = 50
        for i in range(self.x):
            self.board.append([])
            for j in range(self.y):
                self.board[i].append(light)
            
                
        

    def displayBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == True:
                    print("1", end=" ")
                else:
                    print("O", end=" ")
            print()

    
    
    def turnOn(self, a, b, p, q):
        if a == p:
            if b == q:
                if self.board[a][b] == False:
                    self.board[a][b] = True
            else:
                for j in range(b, q+1):
                    print("j : ", j)
                    if self.board[a][j] == False:
                        self.board[a][j] = True
        elif a!=p:
            if b!=q:    
                for i in range(a, p+1):
                    for j in range(b, q+1):
                        if self.board[i][j] == False:
                            self.board[i][j] = True
            else:
                for i in range(a, p):
                    if self.board[i][b] == False:
                        self.board[i][b] = True



    def turnOff(self, a, b, p, q):
        if a == p:
            if b == q:
                if self.board[a][b] == True:
                    self.board[a][b] = False
            else:
                for j in range(b, q+1):
                    print("j : ", j)
                    if self.board[a][j] == True:
                        self.board[a][j] = False
        elif a!=p:
            if b!=q:    
                for i in range(a, p+1):
                    for j in range(b, q+1):
                        if self.board[i][j] == True:
                            self.board[i][j] = False
            else:
                for i in range(a, p):
                    if self.board[i][b] == True:
                        self.board[i][b] = False

    
    def toggle(self, a, b, p, q):
         if a == p:
            if b == q:
                if self.board[a][b] == True:
                    self.board[a][b] = False
                else:
                    self.board[a][b] = True
            else:
                for j in range(b, q+1):
                    print("j : ", j)
                    if self.board[a][j] == True:
                        self.board[a][j] = False
                    else:
                        self.board[a][j] = True
         elif a!=p:
            if b!=q:    
                for i in range(a, p+1):
                    for j in range(b, q+1):
                        if self.board[i][j] == True:
                            self.board[i][j] = False
                        else:
                            self.board[i][j] = True
            else:
                for i in range(a, p+1):
                    if self.board[i][b] == True:
                        self.board[i][b] = False
                    else:
                        self.board[i][b] = True





def readInput(f):
    lines = f.read().splitlines()
    box = []
    for sentence in lines:
        box.append(sentence.split())
        for i in box:
            i.split(',')
    print(box)
    for line in box:
        for word in range(len(line)):
            if line[word] == "turn":
                if line[word+1] == "on":
                    # Do turn on
                    a = line[word+2]
                    b = line[word+3]
                    print(a, b)
                    
                elif line[word+1] == "off":
                    # Do turn off
                    a = line[word+2]
                    b = line[word+3]
                    print(a, b)
            elif line[word] == "toggle":
            # Do toggle
                a = line[word+1]
                b = line[word+2]
                print(a, b)





def main():
    readInput(f=open("input.txt", "r"))
    light = True
   # a = Board(light)
   # a.turnOff(1, 1, 1, 9)
   # a.turnOff(9,1,9,9)
   # a.turnOff(1,1,9,1)
   # a.turnOff(1,9,9,9)
   # a.displayBoard()



























if __name__ == '__main__':
    main()
