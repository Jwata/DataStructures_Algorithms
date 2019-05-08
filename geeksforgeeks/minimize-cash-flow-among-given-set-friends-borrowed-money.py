from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.debts = [[] for _ in range(V)]

    def add_debt(self, i, j, value):
        self.debts[i].append((j, value))

    # O(V^2 + E)
    def minimize_cash_flow(self):
        nets = defaultdict(lambda: 0)

        # O(E)
        for i in range(self.V):
            for j, v in self.debts[i]:
                nets[i] -= v
                nets[j] += v

        g = Graph(self.V)

        # O(V^2)
        while len(nets) > 0:
            max_debtor = None
            max_debt = 0
            max_creditor = None
            max_credit = 0
            for i, v in nets.items():    
                if v > 0 and v > max_credit:
                    max_credit = v
                    max_creditor = i
                elif v < 0 and abs(v) > max_debt:
                    max_debt = abs(v)
                    max_debtor = i
    
            if max_debt > max_credit:
                g.add_debt(max_debtor, max_creditor, max_credit)
                nets.pop(max_creditor)
                nets[max_debtor] += max_credit
                if nets[max_debtor] == 0:
                    nets.pop(max_debtor)
            else:
                g.add_debt(max_debtor, max_creditor, max_debt)
                nets.pop(max_debtor)
                nets[max_creditor] -= max_debt
                if nets[max_creditor] == 0:
                    nets.pop(max_creditor)

        return g

V = 3
g = Graph(V)
g.add_debt(0, 1, 1000)
g.add_debt(0, 2, 2000)
g.add_debt(1, 2, 5000)

g_min = g.minimize_cash_flow()
for i in range(V):
    for j, v in g_min.debts[i]:
        print('debt {}, from {} to {}'.format(v, i, j))
