# A* Search for finding the shortest path between two points in a grid
def heuristic(node, goal):
    # A simple heuristic: Manhattan distance
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star_search(grid, start, goal):
    open_list = [(start, 0)]
    closed_list = set()
    while open_list:
        current, cost = open_list.pop(0)
        if current == goal:
            return current
        closed_list.add(current)
        for neighbor in grid[current]:
            if neighbor not in closed_list:
                open_list.append((neighbor, cost + heuristic(neighbor, goal)))
        open_list.sort(key=lambda x: x[1])
    return None

# Example usage:
grid = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
    (1, 2): [(1, 1), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(1, 1), (2, 0), (2, 2)],
    (2, 2): [(1, 2), (2, 1)]
}

start_node = (0, 0)
goal_node = (2, 2)
goal_reached = a_star_search(grid, start_node, goal_node)
if goal_reached:
    print("Goal reached:", goal_reached)
else:
    print("Goal not reachable")
