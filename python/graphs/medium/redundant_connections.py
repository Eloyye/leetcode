from typing import List

class UnionFind:
    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes + 1) ]
        self.rank = [1]*(num_nodes + 1)

    def find(self, n: int) -> int:
        p = self.parent[n]
        #find root
        while p != self.parent[p]:
            #path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    uf = UnionFind(len(edges))
    for a, b in edges:
        if not self.union(a, b):
            return [a, b]


