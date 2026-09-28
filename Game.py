from random import randint
SHOTS = 5
HITCHANCE = 65 #chance of hitting target in percent

class Player:
    def __init__(self,name,board):
        self.name = name
        self.playerBoard = board

    def getBoard(self):return self.playerBoard
    def getName(self):return self.name
    
def printStart():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             Biathlon\n")
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nYou got",SHOTS,"shots\n")

def printBoard(board):
    print("\n1 2 3 4 5")
    for b in board:
        if b == 1:print("*","",end="")
        else:print(b,"",end="")
    print()

def start(board):
    printStart()
    printBoard(board)


def game():
    board = [1,1,1,1,1]
    start(board)

    hits = 0
    for i in range(1, SHOTS + 1):
        while True:
            try:
                print("\nShot nr",i,"at: ",end="")
                target = int(input())
                if target <=5 and target >= 1:
                    break
                else:
                    print("\nWRITE BETWEEN 1 - 5")
            except(ValueError):
                print("\nWRITE AN INTEGER")
        if randint(0,100) < HITCHANCE: #TODO change so hitchance gets affected after each round
            if(board[target-1] != 0):
                print("\nHit on an open target")
                board[target-1] = 0
                hits+=1
            else:
                print("\nHit on closed target")
        else:
            print("\nMiss")
        printBoard(board)
    print("You hit",hits,"of 5")

def gameRunner():
    while True:
        game()
        print("\nWant to play again? (y/n) ")
        if (input() != "y"):
            break
gameRunner()