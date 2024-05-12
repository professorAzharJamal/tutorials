from networkx import DiGraph

# Create a directed acyclic graph (DAG)
G = DiGraph()
G.add_edge("Sprinkler", "Grass")
G.add_edge("Weather", "Grass")

# Print the nodes and edges
print("Nodes:", G.nodes)
print("Edges:", G.edges)
