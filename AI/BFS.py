from collections import deque

def bfs(graph, start):
  """
  Performs a breadth-first search on a graph.

  Args:
      graph: A dictionary representing the graph, where keys are nodes and values are lists of neighboring nodes.
      start: The starting node for the search.

  Returns:
      None
  """
  queue = deque([start])  # Queue for BFS exploration
  visited = set()
  while queue:
    current_node = queue.popleft()  # Get the next node from the queue
    if current_node not in visited:
      visited.add(current_node)
      print(current_node, end=" -> ")  # Print the current node
      queue.extend(graph[current_node])  # Add neighbors to the queue

# Example usage
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

bfs(graph, 'A')
