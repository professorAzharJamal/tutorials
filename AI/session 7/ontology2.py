import networkx as nx
import matplotlib.pyplot as plt
from rdflib import Graph, Namespace, Literal

# Create a new RDF graph
g = Graph()

# Define namespaces
onto = Namespace("http://example.org/ontology/")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# Add ontology metadata
g.add((onto.Person, rdf.type, rdfs.Class))
g.add((onto.Person, rdfs.subClassOf, onto.Entity))
g.add((onto.Person, rdfs.label, Literal("Person")))

g.add((onto.Entity, rdf.type, rdfs.Class))
g.add((onto.Entity, rdfs.label, Literal("Entity")))

g.add((onto.Organization, rdf.type, rdfs.Class))
g.add((onto.Organization, rdfs.subClassOf, onto.Entity))
g.add((onto.Organization, rdfs.label, Literal("Organization")))

# Create a directed graph
G = nx.DiGraph()

# Add nodes for classes
G.add_node("Entity", label="Entity")
G.add_node("Person", label="Person")
G.add_node("Organization", label="Organization")

# Add edges for subclass relationships
G.add_edge("Person", "Entity", label="subClassOf")
G.add_edge("Organization", "Entity", label="subClassOf")

# Draw the graph
pos = nx.spring_layout(G)  # Layout algorithm
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Display the graph
plt.title("Ontology Graph")
plt.show()
