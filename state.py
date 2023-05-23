import time
import sys


class State:
    def __init__(self):
        self.btk = 0                # backtracking
        self.tme = time.time()      # time
        self.tst = 0                # for test

    def update_bar(self, graph, var=None, val=None):
        domains = graph.domains
        level = len([value for value in graph.assignments if value != 0])
        depth = graph.n
        emoji = '😪'
        if level == depth:
            emoji = '🥳'
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
        # state += ' ' + self.tst
        if var is not None and val is not None:
            state += f' {var}:{val}:{domains[var]}'
        sys.stdout.write('\033[1;32m ' + bar + state + '\r\033[0m')
        sys.stdout.flush()
