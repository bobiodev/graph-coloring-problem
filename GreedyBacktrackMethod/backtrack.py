from graph import Graph
from .heuristic_order import *
from .constraint_process import *
from .state import *

RANDOM: bool
FILTER: bool
JUMPING: bool
JUDGING: bool

graph: Graph
adj: []
domains: []
assignments: []

state: State
domain_log: []
assign_log: []
assign_stack: []


def backtracking(graph: Graph) -> []:

    if 0 not in assignments:
        return assignments

    variable = minimum_remaining_values(graph, RANDOM=RANDOM)
    for value in least_constraining_value(graph, variable, FILTER=FILTER):
        if value not in assignments:
            domains[variable] = {value}

        assignments[variable] = value
        if constraint_checking(graph, variable, value):
            state.forward(graph, variable)
            result = backtracking(graph)
            if result is not None:
                return result
            state.backward()
        assignments[variable] = 0
        state.data_recovery(domains, assignments)

        if JUMPING:
            if state.jumpto is not None:
                if variable != state.jumpto:
                    return None
                state.jumpto = None

    if JUMPING:
        state.jumpto = next((var for var in assign_stack[::-1] if var in adj[variable]), None)
    return None


def backtrack(graph: Graph) -> []:
    global adj, domains, assignments
    adj = graph.adj
    domains = graph.domains
    assignments = graph.assignments

    global state, assign_stack, domain_log, assign_log
    state = graph.state
    domain_log = state.domain_log
    assign_log = state.assign_log
    assign_stack = state.assign_stack

    global RANDOM, FILTER, JUMPING, JUDGING
    RANDOM = state.RANDOM
    FILTER = state.FILTER
    JUMPING = state.JUMPING
    JUDGING = state.JUDGING

    state.tme = time.time()
    solution = backtracking(graph)
    if solution is None:
        state.update_bar(graph, NONE=True)
    print()
    return solution
