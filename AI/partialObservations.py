class Maze:
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

    def get_observation(self, row, col):
        # Simulate partial observation (only see surrounding cells)
        observation = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_move(new_row, new_col):
                observation.append(self.layout[new_row][new_col])
            else:
                observation.append('X')  # Represent unseen cells as 'X'
        return observation

    def solve(self):
        # Simple depth-first search with limited observations
        frontier = [(self.start_row, self.start_col, [])]
        visited = set()
        while frontier:
            current_row, current_col, path = frontier.pop()
            if (current_row, current_col) == (self.goal_row, self.goal_col):
                return path + [(current_row, current_col)]
            if (current_row, current_col) in visited:
                continue
            visited.add((current_row, current_col))
            observation = self.get_observation(current_row, current_col)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = current_row + dr, current_col + dc
                if self.is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
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
