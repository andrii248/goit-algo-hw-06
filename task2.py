import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


# Функція для візуалізації графа з кольоровими ребрами
def draw_graph_step(graph, pos, visited_edges):
    plt.figure()
    G = nx.Graph(graph)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=700,
        font_size=12,
        font_weight="bold",
    )

    red_edges = visited_edges
    blue_edges = [
        (u, v)
        for u in graph
        for v in graph[u]
        if (u, v) not in visited_edges and (v, u) not in visited_edges
    ]

    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color="red", width=2)
    nx.draw_networkx_edges(
        G, pos, edgelist=blue_edges, edge_color="blue", width=2, style="dashed"
    )

    plt.show()


# Реалізація DFS з візуалізацією
def dfs_recursive_visual(graph, vertex, visited=None, visited_edges=None, pos=None):
    if visited is None:
        visited = set()
    if visited_edges is None:
        visited_edges = []
    if pos is None:
        pos = nx.spring_layout(nx.Graph(graph))  # Layout для графа

    visited.add(vertex)
    print(vertex, end=" ")  # Відвідуємо вершину

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited_edges.append((vertex, neighbor))
            draw_graph_step(graph, pos, visited_edges)  # Візуалізація на кожному кроці
            dfs_recursive_visual(graph, neighbor, visited, visited_edges, pos)


# Реалізація BFS (рекурсивно) з візуалізацією
def bfs_recursive_visual(graph, queue, visited=None, visited_edges=None, pos=None):
    if visited is None:
        visited = set()
    if visited_edges is None:
        visited_edges = []
    if pos is None:
        pos = nx.spring_layout(nx.Graph(graph))  # Layout для графа

    if not queue:
        return

    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")  # Відвідуємо вершину
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited_edges.append((vertex, neighbor))
                queue.append(neighbor)
        draw_graph_step(graph, pos, visited_edges)  # Візуалізація на кожному кроці

    bfs_recursive_visual(graph, queue, visited, visited_edges, pos)


# Створення графа (на основі першого прикладу)
graph_data = {
    "New York": ["Boston", "Chicago", "Houston", "Miami"],
    "Boston": ["New York", "Chicago"],
    "Chicago": ["New York", "Boston", "Houston", "Miami"],
    "Houston": ["New York", "Chicago", "Miami"],
    "Miami": ["New York", "Houston", "Chicago"],
}

# Перетворення у формат для networkx
G = nx.Graph()
for node, neighbors in graph_data.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=700,
    font_size=12,
    font_weight="bold",
)
plt.title("Graph Visualization")
plt.show()

# Виконання DFS
print("DFS Path:")
dfs_recursive_visual(graph_data, "New York")

# Виконання BFS
print("\n\nBFS Path:")
bfs_recursive_visual(graph_data, deque(["New York"]))
