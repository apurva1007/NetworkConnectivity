class QuickFind:

    parent = []

    def __init__(self, n):
        self.n = n
        self.count = n
        for i in range(self.n):
            self.parent.append(i)

    def union(self, p, q):
        pid = self.parent[p]
        qid = self.parent[q]

        if pid == qid:
            return

        for i in range(self.n):
            if self.parent[i] == pid:
                self.parent[i] = qid
        self.count -= 1

    def connected(self, p, q):
        print("Connected Components:" , self.count)
        print("Parent Array: ", self.parent)
        print("Is", str(p), "and", str(q), "connected: ", self.parent[p] == self.parent[q])






