from collections import deque

def find_shortest_path(maze, start, end):
  """
  This function finds the shortest path from 'start' to 'end' in a maze using iteration.

  Args:
      maze: A list of lists representing the maze, where 0 represents a walkable path and 1 represents a wall.
      start: A tuple representing the starting coordinates (row, col).
      end: A tuple representing the ending coordinates (row, col).

  Returns:
      A list of coordinates representing the shortest path from start to end, or None if no path exists.
  """

  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, right, down, left

  queue = deque([(start, [start])])  # Queue to store (current cell, path to reach it)
  visited = set()  # Set to keep track of visited cells

  while queue:
    cell, path = queue.popleft()
    if cell == end:
      return path  # Found the end!

    for dx, dy in directions:
      new_row, new_col = cell[0] + dx, cell[1] + dy
      if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
        visited.add((new_row, new_col))
        new_path = path + [(new_row, new_col)]
        queue.append((
            (new_row, new_col), new_path))  # Add next exploration to queue

  # No path found
  return None

# Example usage (same as before)


  # Start exploring from the starting position
  path = [(start[0], start[1])]
  result = explore(start[0], start[1], path)
  return result

# Example usage
maze = [
  [0, 0, 1, 0],
  [1, 0, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0],
]

start = (0, 0)
end = (3, 3)

shortest_path = find_shortest_path(maze, start, end)

if shortest_path:
  print("Shortest Path:", shortest_path)
else:
  print("No Path Found")
