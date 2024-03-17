#Environment - playground for AI agents
#Achieve the goals
#Tic-Tac-Toe
import random

class TicTacToeEnv:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def reset(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        return self.board

    def step(self, action, player):
        # Validate action (not implemented in this simplified example)
        # ...

        self.board[action] = player

        winner = self.check_winner()

        reward = 0
        if winner == player:
            reward = 1
        elif winner is not None:
            reward = -1

        done = all(x != ' ' for x in self.board) and winner is None

        self.current_player = 'O' if player == 'X' else 'X'

        return self.board, reward, done

    def check_winner(self):
        # Check rows, columns, and diagonals
        winning_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                              (0, 3, 6), (1, 4, 7), (2, 5, 8),
                              (0, 4, 8), (2, 4, 6))
        for row in winning_conditions:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != ' ':
                return self.board[row[0]]
        return None

    def get_valid_moves(self):
        """
        Returns a list of available (empty) spaces on the board.
        """
        return [i for i, x in enumerate(self.board) if x == ' ']

# Example usage
env = TicTacToeEnv()
state = env.reset()
print(state)  # Output: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while True:
    # Get player's action
    action = int(input("Enter your move (0-8): "))

    # Take a step in the environment
    next_state, reward, done = env.step(action, 'X')
    print(next_state)

    # Check for game over
    if done:
        if reward == 1:
            print("You win!")
        elif reward == -1:
            print("You lose!")
        else:
            print("It's a draw!")
        break

    # Get opponent's random move
    valid_moves = env.get_valid_moves()
    opponent_move = random.choice(valid_moves)
    print(f"Opponent moves to {opponent_move}")

    # Take opponent's move in the environment
    next_state, reward, done = env.step(opponent_move, 'O')
    print(next_state)

    # ... (continue the game loop)
