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

**Shortest paths using Dijkstra's algorithm:**

- **From New York:**

  - To Chicago: ['New York', 'Chicago'] with total distance 790 miles
  - To Houston: ['New York', 'Houston'] with total distance 1620 miles
  - To Miami: ['New York', 'Miami'] with total distance 1280 miles
  - To Boston: ['New York', 'Boston'] with total distance 215 miles

- **From Chicago:**

  - To New York: ['Chicago', 'New York'] with total distance 790 miles
  - To Houston: ['Chicago', 'Houston'] with total distance 940 miles
  - To Miami: ['Chicago', 'Miami'] with total distance 1380 miles
  - To Boston: ['Chicago', 'Boston'] with total distance 980 miles

- **From Houston:**

  - To New York: ['Houston', 'New York'] with total distance 1620 miles
  - To Chicago: ['Houston', 'Chicago'] with total distance 940 miles
  - To Miami: ['Houston', 'Miami'] with total distance 1180 miles
  - To Boston: ['Houston', 'New York', 'Boston'] with total distance 1835 miles

- **From Miami:**

  - To New York: ['Miami', 'New York'] with total distance 1280 miles
  - To Chicago: ['Miami', 'Chicago'] with total distance 1380 miles
  - To Houston: ['Miami', 'Houston'] with total distance 1180 miles
  - To Boston: ['Miami', 'New York', 'Boston'] with total distance 1495 miles

- **From Boston:**
  - To New York: ['Boston', 'New York'] with total distance 215 miles
  - To Chicago: ['Boston', 'Chicago'] with total distance 980 miles
  - To Houston: ['Boston', 'New York', 'Houston'] with total distance 1835 miles
  - To Miami: ['Boston', 'New York', 'Miami'] with total distance 1495 miles
