import heapq
import unittest
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones) == 1:
        #     return stones[0]
        maxHeap = list(map(lambda elem : -elem, stones))
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x, y = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -abs(y - x))
        return -maxHeap[0] if len(maxHeap) > 0 else 0

class LastStoneWeightTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        input = [2,7,4,1,8,1]
        answer = 1
        self.assertEqual(sol.lastStoneWeight(input), answer)
    def test2(self):
        sol = Solution()
        input = [1]
        answer = 1
        self.assertEqual(sol.lastStoneWeight(input), answer)