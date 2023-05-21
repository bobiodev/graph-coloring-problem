def constraint_checking(graph, var, val):
    adj = graph.adj
    assignments = graph.assignments
    return all(assignments[neighbor] != val for neighbor in adj[var])


def forward_checking(graph, var: int, value: int) -> bool:
    adj = graph.adj
    domains = graph.domains
    assignments = graph.assignments
    domains_log = graph.domains_log
    level = graph.level
    """ Filtering: Forward Checking
        cross off values that violate a constraint
        when added to the existing assignment. """
    for neighbor in adj[var]:
        if assignments[neighbor] == 0 and value in domains[neighbor]:
            domains[neighbor].remove(value)
            domains_log[level].append((neighbor, value))
            if not domains[neighbor]:
                return False
    return True


def arc_consistency_checking(graph) -> bool:
    n = graph.n
    adj = graph.adj
    assignments = graph.assignments
    domains = graph.domains
    domains_log = graph.domains_log
    level = graph.level
    """ this code performs arc consistency checking to eliminate inconsistent values 
        from variable domains in a CSP, which can greatly reduce the search space and 
        improve performance for solving the problem. """

    """ to generate a list of "arcs" (i.e., edges between two variables) 
        where both variables are currently unassigned and the second variable 
        has only one value left in its domain. """
    arcs = [(i, j) for i in range(n) if assignments[i] == 0
            for j in adj[i] if assignments[j] == 0 and len(domains[j]) == 1]
    while arcs:
        """ In each iteration, it selects and removes an arc from the list.
            data structure: stack or queue? stack will fast. """
        (i, j) = arcs.pop()
        """ If the only remaining value in the second variable's domain 
            is not a possible value for the first variable, the arc is skipped. """
        value = domains[j].copy().pop()
        if value not in domains[i]:
            continue
        """ if the remaining value is in the first variable's domain, 
            it is removed from the domain and logged. """
        domains[i].remove(value)
        domains_log[level].append((i, value))
        """ If this leaves the first variable with no possible values, 
            the function returns False, indicating that no valid assignment is possible."""
        if not domains[i]:
            return False
        """ If the first variable now has only one possible value, 
            new arcs are generated from all its unassigned neighbors 
            and added to the list of arcs to be checked."""
        if len(domains[i]) == 1:
            arcs.extend([(k, i) for k in adj[i] if assignments[k] == 0])
    return True
