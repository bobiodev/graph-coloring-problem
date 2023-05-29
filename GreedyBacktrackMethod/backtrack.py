import time

from graph import Graph
from .heuristic_order import *
from .constraint_process import *


def backtracking(graph: Graph) -> []:
    level = graph.level
    domains = graph.domains
    assignments = graph.assignments
    domains_log = graph.domains_log
    assign_log = graph.assign_log
    state = graph.state

    state.update_bar(graph)
    if 0 not in assignments:
        state.update_bar(graph)
        return assignments

    variable = minimum_remaining_values(graph)
    for value in least_constraining_value(graph, variable):
        if value not in assignments:
            domains[variable] = {value}

        assignments[variable] = value
        if constraint_checking(graph, variable, value):
            graph.level += 1
            result = backtracking(graph)
            if result is not None:
                return result
            state.btk += 1
            graph.level -= 1
        assignments[variable] = 0
        while assign_log[level]:
            assignments[assign_log[level].pop()] = 0
        while domains_log[level]:
            (var, val) = domains_log[level].pop()
            domains[var].add(val)
    return None


def backtrack(graph: Graph) -> []:
    graph.state.tme = time.time()
    solution = backtracking(graph)
    print()
    return solution
