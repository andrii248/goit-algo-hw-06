import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
graph = nx.Graph()

# Add nodes (cities)
cities = ["New York", "Chicago", "Houston", "Miami", "Boston"]
graph.add_nodes_from(cities)

# Add edges (transport connections)
connections = [
    ("New York", "Boston", 215),
    ("New York", "Chicago", 790),
    ("Chicago", "Houston", 940),
    ("Houston", "Miami", 1180),
    ("Miami", "New York", 1280),
    ("Boston", "Chicago", 980),
    ("Miami", "Chicago", 1380),
    ("New York", "Houston", 1620),
]

# Add edges with weights (distance in miles)
for city1, city2, distance in connections:
    graph.add_edge(city1, city2, weight=distance)

# Visualize the graph
pos = nx.spring_layout(graph, seed=42)  # Layout for nodes

plt.figure(figsize=(8, 6))

# Draw the graph with weights
nx.draw(
    graph,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
)

# Add edge weights (distances)
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

plt.title("Transport Network between Cities")
plt.show()

# Analyze graph characteristics
num_nodes = graph.number_of_nodes()
num_edges = graph.number_of_edges()
degree_dict = dict(graph.degree())  # Degree of each node

# Corrected calculations
print(f"Number of cities (nodes): {num_nodes}")  # Should be 5
print(f"Number of connections (edges): {num_edges}")  # Should be 8
print("Degrees of each city:")
for city, degree in degree_dict.items():
    print(f"  {city}: {degree}")  # Degree reflects actual edge count per city
