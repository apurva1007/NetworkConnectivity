class QuickUnion:

    parent = []

    def __init__(self, n):
        self.n = n
        self.count = n
        for i in range(self.n):
            self.parent.append(i)

        print(self.parent)

    def find_root(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)

        if root_p == root_q:
            return

        self.parent[root_p] = root_q
        self.count -= 1

    def connected(self, p, q):
        print("Connected Components:" , self.count)
        print("Parent Array: ", self.parent)
        print("Is", str(p), "and", str(q), "connected: ", self.find_root(p) == self.find_root(q))






