# Depth-First Search (DFS)
def dfs(graph, start, goal, visited=[]):
    if start == goal:
        return [start]
    if start not in graph or start in visited:
        return None
    visited.append(start)
    for neighbor in graph[start]:
        path = dfs(graph, neighbor, goal, visited)
        if path is not None:
            return [start] + path
    return None

# Example usage:
maze_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
goal_node = 'F'
path = dfs(maze_graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found")
