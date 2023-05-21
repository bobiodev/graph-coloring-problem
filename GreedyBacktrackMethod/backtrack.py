import time

from graph import Graph
from .heuristic_order import *
from .constraint_process import *


def final_check(graph: Graph, solution: []):
    for var in range(graph.n):
        for neighbor in graph.adj[var]:
            if solution[var] == solution[neighbor]:
                return False
    return True


def backtracking(graph: Graph) -> []:
    graph.level += 1
    level = graph.level
    adj = graph.adj
    domains = graph.domains
    assignments = graph.assignments
    domains_log = graph.domains_log
    state = graph.state
    state.update_bar(graph)

    if 0 not in assignments:
        state.update_bar(graph)
        return assignments

    variable = minimum_remaining_values(graph, MAX_DEGREE=True)
    for value in least_constraining_value(graph, variable):
        if value not in assignments:
            domains[variable] = {value}

        if constraint_checking(graph, variable, value):
            assignments[variable] = value
            if forward_checking(graph, variable, value):
                if arc_consistency_checking(graph):
                    result = backtracking(graph)
                    if result is not None:
                        return result
                    else:
                        state.btk += 1
                        graph.level -= 1
            assignments[variable] = 0
            while domains_log[level]:
                (var, val) = domains_log[level].pop()
                domains[var].add(val)
    return None


def backtrack(graph: Graph) -> []:
    graph.tme = time.time()
    solution = backtracking(graph)
    print()
    if solution:
        print(f'The solution is {final_check(graph, solution)}')
    return solution
