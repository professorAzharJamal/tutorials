def manhattan_distance(start, goal):
  
  x1, y1 = start
  x2, y2 = goal
  return abs(x1 - x2) + abs(y1 - y2)

# Example usage:
maze = [  # This represents a simple maze layout (0 = wall, 1 = open space)
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
]

start = (0, 0)  # Our starting position
goal = (3, 3)  # Our destination

# Calculate the Manhattan distance heuristic (estimated distance to goal)
heuristic_value = manhattan_distance(start, goal)

print(f"Heuristic value (estimated distance to goal): {heuristic_value}")

# In a real application, this heuristic value would be used to guide the search algorithm 
# towards the goal state (exploring paths with lower heuristic values first).