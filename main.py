from graph import Graph
from GreedyBacktrackMethod.backtrack import backtrack


if __name__ == '__main__':
    lastname = input('last name(i.e. 5a, 15b, 25c...) of le450_ > ')
    filename = 'le450_' + lastname
    m = int(lastname[:-1])
    graph = Graph(filename, m)

    solution = backtrack(graph)
    if solution:
        if input('show solution? y/n ') == 'y':
            print(solution)
    else:
        print('No solution')
