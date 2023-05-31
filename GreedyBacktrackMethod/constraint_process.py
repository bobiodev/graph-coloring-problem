def constraint_checking(graph, var, val):
    domains = graph.domains
    assignments = graph.assignments
    level = graph.state.level
    assign_log = graph.assign_log
    n = graph.n
    if forward_checking(graph, var, val) \
            and arc_consistency(graph) \
            and path_consistency(graph):
        """ to reduce the size of the problem by instantly assigning values 
            to the variables which have only one remaining choice. """
        for var in range(n):
            if assignments[var] == 0 and len(domains[var]) == 1:
                assignments[var] = list(domains[var])[0]
                assign_log[level].append(var)
        return True
    else:
        return False


def forward_checking(graph, var: int, value: int) -> bool:
    adj = graph.adj
    domains = graph.domains
    assignments = graph.assignments
    domains_log = graph.domains_log
    level = graph.state.level
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


def arc_consistency(graph) -> bool:
    n = graph.n
    adj = graph.adj
    assignments = graph.assignments
    domains = graph.domains
    domains_log = graph.domains_log
    level = graph.state.level
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
        value = list(domains[j])[0]
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


def path_consistency(graph):
    n = graph.n
    adj = graph.adj
    assignments = graph.assignments
    domains = graph.domains
    """ This code essentially checks for a condition where three unassigned nodes 
        var, x, and y form a path such that they have exactly two colors in their 
        domains and these domains are identical. If such a path exists, it returns 
        False, indicating a violation of Path Consistency, because for a graph 
        coloring problem, at least one node in a triangle (a 3-cycle path) should 
        have more than two colors in its domain to allow a proper 3-coloring. """
    for var in range(n):
        if assignments[var] == 0 and len(domains[var]) == 2:
            for x in adj[var]:
                if assignments[x] == 0 and len(domains[x]) == 2 and domains[x] == domains[var]:
                    for y in adj[x]:
                        if assignments[y] == 0 and y in adj[var] and len(domains[y]) == 2 and domains[y] == domains[x]:
                            return False
    return True
