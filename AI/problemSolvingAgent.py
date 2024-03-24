
maze = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
]


agent_pos = (0, 0) 

goal_pos = (2, 2) 

def valid_move(maze, pos, direction):
  rows, cols = len(maze), len(maze[0])
  new_row, new_col = pos[0] + direction[0], pos[1] + direction[1]
  return 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 1

def move_agent(maze, agent_pos, direction):
  if valid_move(maze, agent_pos, direction):
    new_row, new_col = agent_pos[0] + direction[0], agent_pos[1] + direction[1]
    return (new_row, new_col)
  else:
        return agent_pos

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while agent_pos != goal_pos:
  # Print current maze with agent position
  for row in maze:
    for col in row:
      if (row, col) == agent_pos:
        print("A", end=" ")  
      else:
        print(col, end=" ")
    print()


  for direction in directions:
    new_pos = move_agent(maze, agent_pos, direction)
    if new_pos != agent_pos:
      agent_pos = new_pos
      break  # Stop after successful move


  if agent_pos == goal_pos:
    print("Cheese found!")
    break

print("Maze solved!")