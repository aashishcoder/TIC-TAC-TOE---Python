board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_full():
    for row in board:
        if " " in row:
            return False
    return True

def check_winner(player):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] == PLAYERS[player]:
            return True

    for col in range(len(board)):
        column = [row[col] for row in board]
        if column.count(column[0]) == len(column) and column[0] == PLAYERS[player]:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

PLAYERS = {1: "X", 2: "O"}
player = 1

while True:
    print_board()

    if check_winner(player):
        print(f"Player {player} wins!")
        break

    if check_full():
        print("It's a draw.")
        break

    xcol = int(input(f'In which column would you like your {PLAYERS[player]}?'))
    xrow = int(input(f'In which row would you like your {PLAYERS[player]}?'))

    if 1 <= xcol <= 3 and 1 <= xrow <= 3:
        col = xcol - 1
        row = xrow - 1

        if board[row][col] == " ":
            board[row][col] = PLAYERS[player]
            player = (player % 2) + 1
    else:
        print("Invalid entry. Please try again.")