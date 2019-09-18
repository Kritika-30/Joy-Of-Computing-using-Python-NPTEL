"""
Created on Wed Sep 18 09:08:05 2019

@author: Kritika Singhal
"""

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
#player 1
pl1='X'
#player 2
pl2='O'

# function to enter the symbol in board
def place(symbol):
    print(numpy.matrix(board))
    while True:
        row=int(input('Enter row '))
        col=int(input('Enter column '))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print('Invalid input. Please enter again')
    board[row-1][col-1]=symbol
 
 
def check_row(symbol):
    for row in range(3):
        count=0
        for col in range(3):
            if board[row][col]==symbol:
                count=count+1
            else:
                break
        if count==3:
            return True
    return False
 

def check_col(symbol):
    for col in range(3):
        count=0
        for row in range(3):
            if board[row][col]==symbol:
                count=count+1
            else:
                break
        if count==3:
            return True
    return False
    

def check_dia(symbol):
    count=0
    for i in range(3):
        if board[i][i]==symbol:
            count=count+1
        else:
            break
    if count==3:
        return True
    
    if board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol:
        return True
    return False


def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_dia(symbol)

def play():
    for turn in range(9): 
    # if even player1 chance 
        if turn%2==0:
            print("Player 1 : 'X' chance")
            place(pl1)
            if won(pl1):
                print(numpy.matrix(board))
                print('X won')
                break
        #player 2 chance
        else:     
            print("Player 2 : 'O' chance")
            place(pl2)
            if won(pl2):
                print(numpy.matrix(board))
                print('O won')
                break 
    if not(won(pl1)) and not(won(pl2)):
        print('Draw')
        
play()
