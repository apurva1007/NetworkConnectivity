class FindLargestNodeInTheComponent:

    parent = []
    size = []
    largest = []

    def __init__(self, n):
        self.n = n
        self.count = n
        for i in range(self.n):
            self.parent.append(i)
            self.size.append(1)
            self.largest.append(i)

    def find_root(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        largest_p = self.largest[self.find_root(p)]
        largest_q = self.largest[self.find_root(q)]

        if root_p == root_q:
            return

        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]

            if largest_p > largest_q:
                self.largest[root_q] = largest_p
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

            if largest_q > largest_p:
                self.largest[root_p] = largest_q

        self.count -= 1

        # largest_p = self.largest[p]
        # largest_q = self.largest[q]
        #
        # if largest_p == largest_q:
        #     return
        #
        # for i in range(self.n):
        #     if largest_p > largest_q:
        #         if self.largest[i] == largest_q:
        #             self.largest[i] = largest_p
        #     else:
        #         if self.largest[i] == largest_p:
        #             self.largest[i] = largest_q

    def connected(self, p, q):
        print("Connected Components:", self.count)
        print("Parent Array: ", self.parent)
        print("Size Array: ", self.size)
        print("Largest Array: ", self.largest)
        print("Is", str(p), "and", str(q), "connected: ", self.find_root(p) == self.find_root(q))

    def find(self, p):
        print("Connected Components:", self.count)
        print("Parent Array: ", self.parent)
        print("Size Array: ", self.size)
        print("Largest Array: ", self.largest)
        return self.largest[self.find_root(p)]






