def dfs(graph, start):
  """
  Performs a depth-first search on a graph (iterative approach).

  Args:
      graph: A dictionary representing the graph, where keys are nodes and values are lists of neighboring nodes.
      start: The starting node for the search.

  Returns:
      None
  """
  stack = [start]  # Stack for DFS exploration
  visited = set()
  while stack:
    current_node = stack.pop()  # Get the next node from the stack
    if current_node not in visited:
      visited.add(current_node)
      print(current_node, end=" -> ")  # Print the current node
      stack.extend(reversed(graph[current_node]))  # Add neighbors to the stack in reverse order (avoids bias)

# Example usage
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

dfs(graph, 'A')
