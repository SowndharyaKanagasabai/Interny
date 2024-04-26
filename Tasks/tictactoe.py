'''
Sowndharya Kangasabai
TASK-2
Implement a console-based Tic-Tac-Toe game in Python where
two players take turns making moves.
'''


import random

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def player_input(board, player):
    while True:
        try:
            inp = int(input(f"Player {player}, enter a number 1-9: "))
            if 1 <= inp <= 9 and board[inp - 1] == "_":
                return inp - 1
            else:
                print("Invalid input! Please choose an empty spot (1-9).")
        except ValueError:
            print("Invalid input! Please enter a number.")

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "_":
            return True, board[condition[0]]  # Return the winning player's symbol
    return False, None

def check_tie(board):
    return "_" not in board

def switch_player(player):
    return "O" if player == "X" else "X"

def replay():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")

def tic_tac_toe():
    while True:
        board = ["_" for _ in range(9)]
        player = "X"
        winner = None

        while not winner and not check_tie(board):
            print_board(board)
            position = player_input(board, player)
            board[position] = player
            winner, winning_symbol = check_win(board)  # Unpack winning symbol
            player = switch_player(player)

        print_board(board)
        if winner:
            print(f"Player {winning_symbol} wins!")  # Display the winning player's symbol
        else:
            print("It's a tie!")

        if not replay():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    tic_tac_toe()
