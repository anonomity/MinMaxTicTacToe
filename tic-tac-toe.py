import numpy as np
import random
board = np.empty((3,3), dtype=str)
gameOver = False
depth = 9
print("Tic-Tac-Toe")
print("------------------------------------------------------------")
print(board)
print("------------------------------------------------------------")

visual = np.array([[0,1,2],[3,4,5],[6,7,8]])

def minimax(node, depth, maximizingPlayer):
    pass 

def move(num, player):
    pos = 0
    for i in range(9):
        col = pos % 3
        row = pos // 3
    
        if(visual[row][col] == int(num)):
            if((board[row][col] == 'x') | (board[row][col] == 'o') ):
                print("That space is already occupied")
                return False
            board[row][col] = player 
            evalBoard()
            return True
        
        pos +=1
def winingPrompt(player):
    print("player ", player , " wins!!")
    global gameOver
    gameOver = True
def evalBoard():
    player = ""
    # Checking win by rows
    for row in board:
        player = row[0]
        if((player != '') & (row[1] == player) & (row[2] == player)):
           winingPrompt(player) 
    transBoard = np.transpose(board)
    #checking win by column
    for row in transBoard:
        player = row[0]
        if((player != '') & (row[1] == player) & (row[2] == player)):
            winingPrompt(player) 
    #checking diagonal 
    player = board[1][1]
    if((player != '') & (player == board[0][0]) & (player == board[2][2])):
        winingPrompt(player)
    if((player != '') & (player == board[0][2]) & (player == board[2][0])):
        winingPrompt(player)
def humanMove():
    moves = input("pick a number, where you would like move ")
    move(moves, 'o')
    global depth
    depth -= 1

def computerMove():
    minimax(0,depth,True) 
    global depth
    depth -= 1
    move(num, 'x')
    print(board)
    
while gameOver != True:
    humanMove()
    computerMove()
