# Tic Tac Toe - Two Player Version
# No server
# No networking
# One Python file


def display_board(board):
    print()
    print("     1   2   3")
    print("   +---+---+---+")
    print("1  | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("   +---+---+---+")
    print("2  | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("   +---+---+---+")
    print("3  | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("   +---+---+---+")
    print()


def is_won(board, token):

    # Check rows
    for row in range(3):
        if (board[row][0] == token and
            board[row][1] == token and
            board[row][2] == token):
            return True

    # Check columns
    for col in range(3):
        if (board[0][col] == token and
            board[1][col] == token and
            board[2][col] == token):
            return True

    # Check major diagonal
    if (board[0][0] == token and
        board[1][1] == token and
        board[2][2] == token):
        return True

    # Check other diagonal
    if (board[0][2] == token and
        board[1][1] == token and
        board[2][0] == token):
        return True

    return False


def is_full(board):

    for row in range(3):
        for col in range(3):

            if board[row][col] == " ":
                return False

    return True


def make_move(board, token):

    while True:

        print("Player " + token)

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

        except ValueError:
            print("Please enter numbers only.")
            continue

        # Check row and column
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row and column must be between 1 and 3.")
            continue

        # Check whether square is occupied
        if board[row][col] != " ":
            print("That square is already occupied.")
            continue

        # Place X or O
        board[row][col] = token
        break


# -----------------------------
# MAIN PROGRAM
# -----------------------------

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

current_player = "X"

print("====================")
print("     TIC TAC TOE")
print("====================")

while True:

    display_board(board)

    make_move(board, current_player)

    # Check for winner
    if is_won(board, current_player):

        display_board(board)

        print("Player " + current_player + " won!")
        break

    # Check for draw
    if is_full(board):

        display_board(board)

        print("Game is over, no winner!")
        break

    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"