def max_saturation(graph, variables: []) -> int:
    adj = graph.adj
    assignments = graph.assignments

    saturation = {var: len({assignments[neighbor] for neighbor in adj[var]
                            if assignments[neighbor] != 0}) for var in variables}
    ms = max(saturation.values())
    variables = [var for var in variables if saturation[var] == ms]
    ''' for debug '''
    # for var in variables:
    #     print(f'{var}:{saturation[var]}', end=' ')
    # print('\\')
    # input()
    ''' end debug '''
    return variables[0]


def max_degree(graph, variables: [], DSATUR: bool = True) -> []:
    adj = graph.adj
    assignments = graph.assignments

    """ Sort the variables list according to the degree of each variable. 
        The degree is determined by counting the number of unassigned neighboring variables.
        Reverse order to have the variable with the highest degree at the beginning of the list.
        variables sorted by number of degrees. """

    degrees = {var: sum(assignments[i] == 0 for i in adj[var])
               for var in variables}
    md = max(degrees.values())
    variables = [var for var in variables if degrees[var] == md]

    if not DSATUR or len(variables) == 1:
        return variables[0]
    ''' for debug '''
    # for var in variables[:5]:
    #     print(f'{var}:{sum(assignments[i] == 0 for i in adj[var])}', end=' ')
    # print()
    # input()
    ''' end debug '''
    return max_saturation(graph, variables)


def minimum_remaining_values(graph, MAX_DEGREE: bool = True) -> int:
    n = graph.n
    adj = graph.adj
    domains = graph.domains
    assignments = graph.assignments

    """ Minimum Remaining Values (MRV) heuristic for variable ordering
        The MRV heuristic selects the variable with the smallest domain 
        (i.e., fewest remaining legal values) for assignment next. """

    variables = [var for var in range(n) if assignments[var] == 0]
    mrv = len(domains[min(variables, key=lambda var: len(domains[var]))])
    variables = [var for var in variables if len(domains[var]) == mrv]

    if not MAX_DEGREE or len(variables) == 1:
        return variables[0]
    ''' for debug'''
    # print('\\ find next variable')
    # for var in variables[:10]:
    #     print(f'{var}:{len(domains[var])}', end=' ')
    # print()
    ''' end debug '''
    return max_degree(graph, variables)


def least_constraining_value(graph, var: int) -> [int]:
    adj = graph.adj
    domains = graph.domains
    level = graph.level
    m = graph.m
    """ Least Constraining Value (LCV) heuristic for value ordering. 
        The LCV heuristic orders the values in the domain of the variable 
        to be assigned based on the number of conflicts each value would 
        create in the remaining unassigned variables. 
        The values that would create fewer conflicts are ordered first. """
    if len(domains[var]) == 1:
        return domains[var]
    # for le450_5a, 5b...
    if m <= 5:
        values = sorted(domains[var],
                        key=lambda value:
                        sum(value in domains[neighbor] for neighbor in adj[var]))
        return values
    # for le450_15a, 15b, 25a...
    """ to computes a measure of conflict for each possible value of the variable, 
        determines an average conflict level, and then constructs a sorted list 
        of those values that cause less-equal-than-average conflicts. """
    # conflicts as c is a dict
    # for c.key in domains[var]
    # c.value is number of c.key's conflicts
    conflicts = {value: sum(value in domains[neighbor]
                            for neighbor in adj[var])
                 for value in domains[var]}
    average = sum(conflicts.values()) / len(conflicts)
    values = sorted([value for value in conflicts.keys() if conflicts[value] <= average],
                    key=lambda value: conflicts[value])
    ''' for debug '''
    # for value in values:
    #     print(f'{value}:{conflicts[value]}', end=' ')
    # input()
    # print()
    ''' end debug '''
    return values
