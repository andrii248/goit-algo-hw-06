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

# Perform DFS and BFS
start_city = "New York"

# Depth-First Search (DFS)
print("DFS Path:")
dfs_path = list(nx.dfs_edges(graph, source=start_city))
for edge in dfs_path:
    print(f"{edge[0]} -> {edge[1]}")

# Breadth-First Search (BFS)
print("\nBFS Path:")
bfs_path = list(nx.bfs_edges(graph, source=start_city))
for edge in bfs_path:
    print(f"{edge[0]} -> {edge[1]}")

# Explanation of differences
print("\nExplanation:")
print(
    "DFS explores as far as possible along each branch before backtracking. This results in a path that can go deep into the graph before exploring other branches."
)
print(
    "BFS explores all neighbors at the current depth before moving deeper, resulting in a level-by-level exploration of the graph."
)
