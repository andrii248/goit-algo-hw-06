def dijkstra(graph, start):
    # Initialize distances and the set of unvisited vertices
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Find the vertex with the smallest distance among unvisited vertices
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # If the smallest distance is infinity, we are done
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Update the shortest path if the new distance is shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Remove the current vertex from the set of unvisited vertices
        unvisited.remove(current_vertex)

    return distances


# Graph representation with weights using a dictionary
graph = {
    "New York": {"Boston": 215, "Chicago": 790, "Houston": 1620, "Miami": 1280},
    "Boston": {"New York": 215, "Chicago": 980},
    "Chicago": {"New York": 790, "Boston": 980, "Houston": 940, "Miami": 1380},
    "Houston": {"New York": 1620, "Chicago": 940, "Miami": 1180},
    "Miami": {"New York": 1280, "Houston": 1180, "Chicago": 1380},
}

# Compute shortest paths between all pairs of vertices
all_shortest_paths = {}
for vertex in graph.keys():
    all_shortest_paths[vertex] = dijkstra(graph, vertex)

# Print the results as a table
print("\nShortest connections between cities\n")
print(f"{'From/To':<12} {'  '.join(graph.keys()):<50}")
print("-" * 62)
for start, distances in all_shortest_paths.items():
    row = f"{start:<15} "
    row += "  ".join(f"{distances[dest]:<5}" for dest in graph.keys())
    print(row)
