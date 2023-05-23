from graph import Graph
from GreedyBacktrackMethod.backtrack import backtrack


def final_check(graph: Graph, solution: []):
    for var in range(graph.n):
        for neighbor in graph.adj[var]:
            if solution[var] == solution[neighbor]:
                return False
    return True


if __name__ == '__main__':
    filename = 'le450_' + input('last name(i.e. 5a, 15b, 25c...) of le450_ > ')
    graph = Graph(filename)

    solution = backtrack(graph)

    if solution:
        print(f'The solution is {final_check(graph, solution)}')
        if input('show solution? y/n ') == 'y':
            print(solution)
    else:
        print('No solution')
