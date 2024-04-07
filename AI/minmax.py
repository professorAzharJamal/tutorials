import numpy as np

# Constants representing players
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

# Constants representing board dimensions
ROWS = 6
COLS = 7

def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

def print_board(board):
    print(np.flip(board, 0))  # Flip the board to display from bottom to top

def is_valid_move(board, col):
    return board[ROWS - 1][col] == EMPTY

def drop_piece(board, col, player):
    for row in range(ROWS):
        if board[row][col] == EMPTY:
            board[row][col] = player
            break

def check_winner(board, player):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and \
               board[row][col+1] == player and \
               board[row][col+2] == player and \
               board[row][col+3] == player:
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == player and \
               board[row+1][col] == player and \
               board[row+2][col] == player and \
               board[row+3][col] == player:
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == player and \
               board[row+1][col+1] == player and \
               board[row+2][col+2] == player and \
               board[row+3][col+3] == player:
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and \
               board[row-1][col+1] == player and \
               board[row-2][col+2] == player and \
               board[row-3][col+3] == player:
                return True

    return False

def evaluate_board(board, player):
    if check_winner(board, player):
        return 100
    elif check_winner(board, 3 - player):  # Opponent winning
        return -100
    else:
        return 0

def minimax(board, depth, maximizingPlayer):
    if depth == 0 or is_game_over(board):
        return evaluate_board(board, PLAYER_X)

    if maximizingPlayer:
        maxEval = float('-inf')
        for col in range(COLS):
            if is_valid_move(board, col):
                new_board = board.copy()
                drop_piece(new_board, col, PLAYER_X)
                eval = minimax(new_board, depth - 1, False)
                maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for col in range(COLS):
            if is_valid_move(board, col):
                new_board = board.copy()
                drop_piece(new_board, col, PLAYER_O)
                eval = minimax(new_board, depth - 1, True)
                minEval = min(minEval, eval)
        return minEval

def is_game_over(board):
    return check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O) or np.all(board != EMPTY)

def get_best_move(board, depth):
    best_score = float('-inf')
    best_move = None
    for col in range(COLS):
        if is_valid_move(board, col):
            new_board = board.copy()
            drop_piece(new_board, col, PLAYER_X)
            score = minimax(new_board, depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = col
    return best_move

# Example usage
if __name__ == "__main__":
    board = create_board()
    print("Initial board:")
    print_board(board)
    while not is_game_over(board):
        col = int(input("Enter your move (column 0-6): "))
        if is_valid_move(board, col):
            drop_piece(board, col, PLAYER_O)
            print("Updated board after your move:")
            print_board(board)
            if is_game_over(board):
                break
            print("AI is thinking...")
            best_move = get_best_move(board, depth=4)  # Adjust depth for difficulty
            print(f"AI's move: {best_move}")
            drop_piece(board, best_move, PLAYER_X)
            print("Updated board after AI's move:")
            print_board(board)
        else:
            print("Invalid move! Try again.")
    if check_winner(board, PLAYER_X):
        print("AI wins!")
    elif check_winner(board, PLAYER_O):
        print("You win!")
    else:
        print("It's a draw!")
