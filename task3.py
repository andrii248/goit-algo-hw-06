import networkx as nx

# Create the graph (imported from the first task)
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

# Implement Dijkstra's algorithm to find shortest paths
print("Shortest paths using Dijkstra's algorithm:")
for source in cities:
    for target in cities:
        if source != target:
            shortest_path = nx.dijkstra_path(
                graph, source=source, target=target, weight="weight"
            )
            path_length = nx.dijkstra_path_length(
                graph, source=source, target=target, weight="weight"
            )
            print(
                f"Shortest path from {source} to {target}: {shortest_path} with total distance {path_length} miles"
            )
