class Chessboard:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, start_pos, end_pos):
        if not self.is_valid_position(start_pos) or not self.is_valid_position(end_pos):
            return False
        piece = self.board[start_pos[0]][start_pos[1]]
        return piece != ' '  # For simplicity, any move from a non-empty square is considered valid

    def move_piece(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            piece = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = ' '
            self.board[end_pos[0]][end_pos[1]] = piece
            return True
        return False

    def is_valid_position(self, pos):
        row, col = pos
        return 0 <= row < 8 and 0 <= col < 8

def get_move_input():
    start = input("Enter start position (row col): ").split()
    end = input("Enter end position (row col): ").split()
    return (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))

def play_chess():
    board = Chessboard()
    player = 'White'  # Start with White player
    while True:
        print("\nCurrent board:")
        board.print_board()
        if player == 'White':
            print("White's turn:")
        else:
            print("Black's turn:")
        start_pos, end_pos = get_move_input()
        if board.move_piece(start_pos, end_pos):
            print("Move successful!")
            # Switch player
            player = 'Black' if player == 'White' else 'White'
        else:
            print("Invalid move!")

if __name__ == "__main__":
    play_chess()