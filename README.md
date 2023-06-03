# Graph Coloring Problem

This repository, graph-coloring-problem, focuses on implementing and studying a collection of algorithms to address the
Graph Coloring Problem. The Graph Coloring Problem is a classic and computationally challenging problem in computer
science and combinatorics, where we aim to assign colors to the vertices of a graph such that no two adjacent vertices
share the same color.

## Getting Started

This project requires Python interpreter version 3.5 or above.
To run the project, execute the following command:

```bash
python main.py
# or
python3 main.py
```

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

### Path Consistency

Path consistency in graph coloring ensures that if a path between two vertices can be colored
consistently, the endpoints can share a color. This simplifies the problem by eliminating
invalid color choices, reducing computational complexity, and increasing efficiency of finding
a solution.

## Test

| file          | min colors | techniques enable | best scenario time | backtracking |
|---------------|------------|-------------------|--------------------|--------------|
| le450_5a.col  | 5          | -                 | 0.3s               | 166          |
| le450_5b.col  | 5          | -                 | 0.1s               | 4            |
| le450_5c.col  | 5          | -                 | 0.1s               | 6            |
| le450_5d.col  | 5          | -                 | 0.1s               | 0            |
| le450_15a.col | 15         | rfj               | 1.99hrs            | 14265710     |
| le450_15b.col | 15         | rfj               | 0.1s               | 0            |
| le450_15c.col | 22         | rfj               | 3.9s               | 3971         |
| le450_15d.col | 23         | rfj               | 0.8s               | 663          |
| le450_25a.col | 25         | -                 | 0.2s               | 0            |
| le450_25b.col | 25         | -                 | 0.2s               | 0            |
| le450_25c.col | 27         | j                 | 2.0s               | 1422         |
| le450_25d.col | 27         | rfj               | 12.0s              | 12478        |

## Usage

Please refer to the individual documentation for each algorithm within the repository for specific usage and
implementation details.

This project serves as a comprehensive resource for anyone interested in the Graph Coloring Problem, providing a robust
set of strategies to tackle this intriguing problem. It is also a valuable tool for comparative analysis of different
algorithms under various problem configurations.

Feel free to explore, use, and contribute to this project.
