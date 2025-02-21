import tkinter as tk
from tkinter import messagebox

current_player = "X"  # Global variable to track the current player
board = [["" for _ in range(3)] for _ in range(3)]  # Track board state

#Check Winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":  # Row check
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":  # Column check
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

#Switch Between X and 0 and restart if game over
def on_button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

#Reset Board
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

# Configure rows and columns to expand equally
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Create 9 buttons in a 3x3 grid
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 14), width=5, height=2,
                                      command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].grid(row=row, column=col, sticky="nsew")

root.mainloop()
