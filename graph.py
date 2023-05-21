from state import State
import re


class Graph:
    def __init__(self, filename):
        self.adj = get_graph(filename)
        self.n = len(self.adj)
        self.m = int(re.findall(r'\d+', filename)[1])
        self.domains = [
            {value + 1 for value in range(self.m)}
            for variable in range(self.n)
        ]
        self.assignments = [0 for variable in range(self.n)]
        self.domains_log = [[] for level in range(self.n)]
        self.level = -1
        self.state = State()


def get_graph(filename):
    print(f'file: {filename}')
    pathname = 'graphs/' + filename + '.col'
    nodes = edges = 0
    adj: [set]
    with open(pathname, 'r') as f:
        for line in f.readlines():
            if line[0] == 'c':
                continue
            if line[0] == 'p':
                parts = line.split(' ')
                nodes = int(parts[2])
                edges = int(parts[3])
                adj = [set() for _ in range(nodes)]
            elif line[0] == 'e':
                parts = line.split(' ')
                i = int(parts[1])
                j = int(parts[2])
                i -= 1
                j -= 1
                adj[i].add(j)
                adj[j].add(i)
        print(f'edges: {edges}')
        print(f'nodes: {nodes}')
        print(f'color: {filename[6:-1]}')
    return adj
