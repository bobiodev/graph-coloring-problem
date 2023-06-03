import time
import sys


class State:
    def __init__(self, graph):
        # for test
        self.tst = 0
        # backtracking
        self.btk = 0
        # time
        self.tme = time.time()
        # recursion stack depth
        self.level = 0
        # for backjumping
        self.assign_stack = []
        self.jumpto = None
        # assign & domain log for recovering
        self.assign_log = [[] for _ in range(graph.n)]
        self.domain_log = [[] for _ in range(graph.n)]
        # constants
        self.FILTER = True
        self.RANDOM = True
        self.JUMPING = True
        self.JUDGING = True

    def update_bar(self, graph, NONE=False):
        level = len([value for value in graph.assignments if value != 0])
        depth = graph.n
        emoji = '😪'
        if level == depth:
            emoji = '🥳'
        elif NONE:
            emoji = '😵'
        p = int(level / depth * 100)
        q = 99 - p
        r = '-'
        if p <= 50:
            left = r * (p // 2) + " " * ((q // 2) - 24)
            right = " " * 25
        else:
            left = r * 25
            right = r * ((p // 2) - 24) + ' ' * (q // 2)
        if p < 10:
            left += ' '
        elif p == 100:
            right = right.replace('--', '', 1)
        bar = '[' + left + str(p) + "%" + emoji + right + ']'
        tme = time.time() - self.tme
        state = ' ' + str(round(tme, 1)) + 's'
        state += ' ⤴ ' + str(self.btk)
        # state += ' ' + str(self.jumpto)
        sys.stdout.write('\033[1;32m ' + bar + state + '\r\033[0m')
        sys.stdout.flush()

    def forward(self, graph, var):
        self.level += 1
        self.assign_stack.append(var)
        self.update_bar(graph)

    def backward(self):
        self.level -= 1
        self.assign_stack.pop()
        self.btk += 1

    def data_recovery(self, domains, assignments):
        while self.assign_log[self.level]:
            assignments[self.assign_log[self.level].pop()] = 0
        while self.domain_log[self.level]:
            (var, val) = self.domain_log[self.level].pop()
            domains[var].add(val)
