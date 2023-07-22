from typing import List
import unittest

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.rank = [1]*(n + 1)
    def find(self, u : int) -> int:
        parent = self.parents[u]
        while parent != self.parents[parent]:
            #path compression
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    def union(self, u : int, v: int) -> bool:
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] > self.rank[v_root]:
            self.parents[v_root] = u_root
            self.rank[u_root] += self.rank[v_root]
        else:
            self.parents[u_root] = v_root
            self.rank[v_root] += self.rank[u_root]
        return True

def numConnectedComponents(n : int, edges: List[List[int]]) -> int:
    numComponents = n
    dsu = UnionFind(n)
    for u, v in edges:
        numComponents = numComponents - 1 if dsu.union(u, v) else numComponents
    return numComponents
def validTree(n : int, edges: List[List[int]]) -> bool:
    #check property of tree
    if n - 1 != len(edges):
        return False
    #check connected components
    return numConnectedComponents(n, edges) == 1

class ValidTreeGraphTests(unittest.TestCase):
    def test1(self):
        n = 5
        edges = [[0,1],[0,2],[0,3],[1,4]]
        self.assertTrue(validTree(n, edges))
    def test2(self):
        n = 5
        edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        self.assertFalse(validTree(n, edges))
    def test3(self):
        #disconnected graph with n-1 edges
        n = 5
        edges = [[0,1],[1,2],[3,4]]
        self.assertFalse(validTree(n, edges))
    def test4(self):
        n = 1
        edges = []
        self.assertTrue(validTree(n, edges))