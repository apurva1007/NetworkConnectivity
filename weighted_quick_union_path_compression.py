class WeightedQuickUnionPathCompression:

    parent = []
    size = []

    def __init__(self, n):
        self.n = n
        self.count = n
        for i in range(self.n):
            self.parent.append(i)
            self.size.append(1)

    def find_root(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)

        if root_p == root_q:
            return

        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        self.count -= 1

    def connected(self, p, q):
        print("Connected Components:" , self.count)
        print("Parent Array: ", self.parent)
        print("Size Array: ", self.size)
        print("Is", str(p), "and", str(q), "connected: ", self.find_root(p) == self.find_root(q))






