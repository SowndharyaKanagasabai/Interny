'''
Sowndharya Kangasabai
TASK-2
Implement a console-based Tic-Tac-Toe game in Python where
two players take turns making moves.
'''

import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("___________")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("___________")
    print(board[6]+" | "+board[7]+" | "+board[8])

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in the spot!")

def checkColumn(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    return False

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checkTie(board):
    if "_" not in board:
        printBoard(board)
        print("It is a tie!")
        return True
    return False

def checkWin():
    if checkDiag(board) or checkColumn(board) or checkRow(board):
        return True
    return False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin() or checkTie(board):
        printBoard(board)
        if checkWin():
            print(f"The winner is {winner}")
        break
    switchPlayer()
    computer(board)
    if checkWin() or checkTie(board):
        printBoard(board)
        if checkWin():
            print(f"The winner is {winner}")
        break
