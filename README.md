# Graph Coloring Problem

This repository, graph-coloring-problem, focuses on implementing and studying a collection of algorithms to address the
Graph Coloring Problem. The Graph Coloring Problem is a classic and computationally challenging problem in computer
science and combinatorics, where we aim to assign colors to the vertices of a graph such that no two adjacent vertices
share the same color.

## Algorithms

In our approach to solving the Graph Coloring Problem, we have implemented a variety of algorithms, each with its unique
strengths, which include:

### Backtracking

A fundamental algorithm that explores all possible coloring configurations to find a solution. While it can be
computationally expensive, it serves as a basis for many other advanced techniques.

### Minimum Remaining Values (MRV)

An optimization strategy that chooses the vertex with the fewest remaining valid colors to color next.

### Least Constraining Value (LCV)

Another heuristic strategy that selects the color that leaves the most freedom for subsequent vertex colorings.

### Degree Heuristic

A heuristic that prioritizes coloring vertices with the highest degree (the most edges connected to it), which is based
on the logic that they pose the most constraints.

### Forward Checking

This technique checks whether a future assignment is possible before making a current assignment.

### Arc Consistency (AC)

An advanced constraint propagation technique that reduces the search space by eliminating values from the domains of
unassigned vertices.

## Test

| file          | backtracks | time  | memory |
|---------------|------------|-------|--------|
| le450_5a.col  | 166        | 266ms | 16MB   |
| le450_5b.col  | 4          | 49ms  | 16MB   |
| le450_5c.col  | 6          | 76ms  | 16MB   |
| le450_5d.col  | 0          | 58ms  | 16MB   |
| le450_15a.col |            |       |        |
| le450_15b.col | 182        | 251ms | 16MB   |
| le450_15c.col |            |       |        |
| le450_15d.col |            |       |        |
| le450_25a.col | 0          | 178ms | 16MB   |
| le450_25b.col | 0          | 181ms | 16MB   |
| le450_25c.col |            |       |        |
| le450_25d.col |            |       |        |

## Usage

Please refer to the individual documentation for each algorithm within the repository for specific usage and
implementation details.

This project serves as a comprehensive resource for anyone interested in the Graph Coloring Problem, providing a robust
set of strategies to tackle this intriguing problem. It is also a valuable tool for comparative analysis of different
algorithms under various problem configurations.

Feel free to explore, use, and contribute to this project.
