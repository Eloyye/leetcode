from typing import List
import unittest as ut
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [1]*(size + 1)
        self.numConnectedComponents = size
    def findRoot(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            #path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent
        return p

    def union(self, a, b):
        r1, r2 = self.findRoot(a), self.findRoot(b)
        if r1 == r2:
            return False
        if self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
            self.rank[r1] += self.rank[r2]
            self.numConnectedComponents -= 1
        else:
            self.parent[r1] = r2
            self.rank[r2] = self.rank[r1]
            self.numConnectedComponents -= 1
        return True

def countComponents(n : int, edges: List [List[int]])-> int:
    dsu = UnionFind(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.numConnectedComponents

class CountComponentsTest(ut.TestCase):
    def test1(self):
        n = 5
        edges = [[0,1],[1,2],[3,4]]
        self.assertEqual(countComponents(n, edges), 2)
    def test2(self):
        n = 5
        edges = [[0,1],[1,2],[2,3],[3,4]]
        self.assertEqual(countComponents(n, edges), 1)
