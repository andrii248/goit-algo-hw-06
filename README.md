# Transport Network Analysis

## Task 1: Graph Creation and Analysis

### Description

Create a graph representing a transport network between five cities. The graph includes nodes as cities and edges as transport connections with distances (weights).

### Results

- **Number of cities (nodes):** 5
- **Number of connections (edges):** 8
- **Degrees of each city:**
  - New York: 4
  - Chicago: 4
  - Houston: 3
  - Miami: 3
  - Boston: 2

---

## Task 2: DFS and BFS Pathfinding

### Description

Implement Depth-First Search (DFS) and Breadth-First Search (BFS) to explore the graph starting from New York. Compare the paths obtained from both algorithms.

### Results

- **DFS Path:**

  - New York -> Boston
  - Boston -> Chicago
  - Chicago -> Houston
  - Houston -> Miami

- **BFS Path:**
  - New York -> Boston
  - New York -> Chicago
  - New York -> Miami
  - New York -> Houston

### Explanation

- **DFS** explores as far as possible along each branch before backtracking. This results in a path that goes deep into the graph before exploring other branches.
- **BFS** explores all neighbors at the current depth before moving deeper, resulting in a level-by-level exploration of the graph.

---

## Task 3: Shortest Path Using Dijkstra's Algorithm

### Description

Use Dijkstra's algorithm to compute the shortest path between all pairs of cities in the transport network. The graph includes distances (weights) on edges.

### Results

### Shortest Distance Between Cities:

| From/To      | New York | Boston | Chicago | Houston | Miami |
| ------------ | -------- | ------ | ------- | ------- | ----- |
| **New York** | 0        | 215    | 790     | 1620    | 1280  |
| **Boston**   | 215      | 0      | 980     | 1920    | 1495  |
| **Chicago**  | 790      | 980    | 0       | 940     | 1380  |
| **Houston**  | 1620     | 1920   | 940     | 0       | 1180  |
| **Miami**    | 1280     | 1495   | 1380    | 1180    | 0     |
