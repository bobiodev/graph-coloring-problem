n: int
adj: []
domains: []
assignments: []
assign_log: []
domain_log: []
level: int


def constraint_checking(graph, var, val) -> bool:

    global n, adj, domains, assignments, assign_log, domain_log, level
    n = graph.n
    adj = graph.adj
    domains = graph.domains
    assignments = graph.assignments
    assign_log = graph.state.assign_log
    domain_log = graph.state.domain_log
    level = graph.state.level

    if forward_checking(var, val) and arc_consistency() and path_consistency():
        for var in range(n):
            if assignments[var] == 0 and len(domains[var]) == 1:
                assignments[var] = next(iter(domains[var]))
                assign_log[level].append(var)
        return True
    return False


def forward_checking(var: int, value: int) -> bool:

    """ The Forward-Checking proactively eliminates conflicting
        colors from neighboring nodes after each assignment,
        reducing backtracking and enhancing efficiency. """

    for neighbor in adj[var]:
        if assignments[neighbor] == 0 and value in domains[neighbor]:
            domains[neighbor].remove(value)
            domain_log[level].append((neighbor, value))
            if not domains[neighbor]:
                return False
    return True


def arc_consistency() -> bool:

    """ The Arc-Consistency refines domains of variables before assignments by
        iteratively removing inconsistent values from each variable's domain,
        it ensures that every possible assignment is consistent with the coloring
        constraints, leading to a solution space that is easier to navigate and
        reducing the need for backtracking. """

    arcs = [(i, j) for i in range(n) if assignments[i] == 0
            for j in adj[i] if assignments[j] == 0 and len(domains[j]) == 1]
    while arcs:
        (i, j) = arcs.pop()
        value = next(iter(domains[j]))
        if value in domains[i]:
            domains[i].remove(value)
            domain_log[level].append((i, value))
            if not domains[i]:
                return False
            elif len(domains[i]) == 1:
                arcs.extend([(k, i) for k in adj[i] if assignments[k] == 0])
    return True


def path_consistency() -> bool:

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
