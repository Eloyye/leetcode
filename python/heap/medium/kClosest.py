import heapq
import math
import unittest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x:int, y:int) -> float:
            return x**2 + y**2
        #use max heap
        maxHeap = [ (-distance(p[0], p[1]), p) for p in points]
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        return [tup[1] for tup in maxHeap]

class KClosestTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        input = [[1,3],[-2,2]]
        k = 1
        out = sol.kClosest(input, k)
        expected = [[-2,2]]
        self.assertEqual(out, expected)
    def test2(self):
        sol = Solution()
        input = [[3,3],[5,-1],[-2,4]]
        k = 2
        out = sol.kClosest(input, k)
        expected = [[-2,4],[3,3]]
        self.assertEqual(out.sort(), expected.sort())

