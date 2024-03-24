import random

class Maze:
  """
  Represents a simple maze with walls (#), start (S), and goal (E).
  """
  def __init__(self, layout):
    self.layout = layout
    self.rows, self.cols = len(layout), len(layout[0])
    self.start_row, self.start_col = self.find_start(layout)
    self.goal_row, self.goal_col = self.find_goal(layout)

  def find_start(self, layout):
    for row in range(self.rows):
      for col in range(self.cols):
        if layout[row][col] == 'S':
          return row, col
    raise ValueError("Start position (S) not found in maze layout")

  def find_goal(self, layout):
    for row in range(self.rows):
      for col in range(self.cols):
        if layout[row][col] == 'E':
          return row, col
    raise ValueError("Goal position (E) not found in maze layout")

  def is_valid_move(self, row, col):
    return 0 <= row < self.rows and 0 <= col < self.cols and self.layout[row][col] != '#'

  def get_possible_moves(self, row, col):
    """
    Simulates non-determinism: Returns a list of possible next positions
    with their corresponding probabilities of success.
    """
    moves = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      new_row, new_col = row + dr, col + dc
      if self.is_valid_move(new_row, new_col):
        # Simulate a success probability (adjust as needed)
        success_prob = random.uniform(0.7, 1.0)  # 70% to 100% chance of success
        moves.append((new_row, new_col, success_prob))
    return moves

  def solve(self):
    """
    Simple Depth-First Search with non-deterministic actions.
    Considers success probabilities when exploring possible moves.
    """
    frontier = [(self.start_row, self.start_col, [])]
    visited = set()
    while frontier:
      current_row, current_col, path = frontier.pop()
      if (current_row, current_col) == (self.goal_row, self.goal_col):
        return path + [(current_row, current_col)]
      if (current_row, current_col) in visited:
        continue
      visited.add((current_row, current_col))
      for new_row, new_col, success_prob in self.get_possible_moves(current_row, current_col):
        # Consider success probability during exploration
        if random.random() < success_prob:  # Succeed in the move with given probability
          frontier.append((new_row, new_col, path + [(current_row, current_col)]))
    return None  # No solution found

# Example maze layout
maze_layout = [
    ['#', ' ', ' ', ' ', '#'],
    [' ', 'S', '#', ' ', ' '],
    [' ', ' ', '#', ' ', ' '],
    [' ', '#', ' ', '#', 'E'],
    ['#', ' ', ' ', '#', '#'],
]

maze = Maze(maze_layout)
solution = maze.solve()

if solution:
  print("Found solution:", solution)
else:
  print("No solution found")