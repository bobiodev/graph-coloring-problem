from graph import Graph
from GreedyBacktrackMethod.backtrack import backtrack


if __name__ == '__main__':
    filename = 'le450_' + input('last name(i.e. 5a, 15b, 25c...) of le450_ > ')
    graph = Graph(filename)

    solution = backtrack(graph)
    if solution:
        if input('show solution? y/n ') == 'y':
            print(solution)
    else:
        print('No solution')
