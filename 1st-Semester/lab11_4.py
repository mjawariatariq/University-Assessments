import sys
import random
board=['-','-','-','-','-','-','-','-','-']
p1=""
p2=""

def player_won(s):
    if ((board[0]==s and board[1]==s and board[2]==s) or(board[3]==s and board[4]==s and board[5]==s) or(board[6]==s and board[7]==s and board[8]==s) or(board[0]==s and board[3]==s and board[6]==s) or (board[1]==s and board[4]==s and board[7]==s) or(board[2]==s and board[5]==s and board[8]==s)or(board[0]==s and board[4]==s and board[8]==s)or(board[2]==s and board[4]==s and board[6]==s)):
        return True
    else:
        return False
def draw():
    for item in board:
        if item=="-":
            return False
    return True
    
def display_board():
    print("The current board position is: ")
    count=0
    for i in range(len(board)):
        print(board[i],end="  ")
        count+=1
        if count%3==0:
            print()

def update_board(idx,val):
    board[idx]=val


def playGame():
    print("Tic-tac-toe game (23 AI)")
    display_board()
    p1=input("Please select your symbol (o or x)")
    if p1=="o":
        p2="x"
    elif p1=="x":
        p2="o"
    else:
        print("Invalid selection")
        exit(0)
    turn=random.randrange(1,2)
    while not(player_won(p1) or player_won(p2) or draw()):
        if turn==1:
            move=int(input("Player 1: enter your move (0-8)"))
            update_board(move,p1)
            display_board()
            turn=2
            if player_won(p1):
                print("Player 1 won!")
                break

        if turn==2:
            move=int(input("Player 2: enter your move (0-8)"))
            update_board(move,p2)
            display_board()
            turn=1
            if player_won(p2):
                print("Player 2 won!")
                break 
           
playGame()
