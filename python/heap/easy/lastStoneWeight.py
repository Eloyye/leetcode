import heapq
import unittest
from typing import List


class MaxHeap:
    def __init__(self, input_list):
        self.max_heap = list(map(lambda elem: -elem, input_list))
        heapq.heapify(self.max_heap)
    def pop(self):
        return -1 * heapq.heappop(self.max_heap)
    def push(self, val):
        heapq.heappush(self.max_heap, -1 * val)
    def get_head(self):
        return -1 * self.max_heap[0]
    def get_length(self):
        return len(self.max_heap)

class Solution:
    def lastStoneWeight2(self, stones: List[int]) -> int:
        max_heap = MaxHeap(stones)
        while max_heap.get_length() > 1:
            x, y = max_heap.pop(), max_heap.pop()
            if x != y:
                max_heap.push(abs(x - y))
        return max_heap.get_head() if max_heap.get_length() > 0 else 0

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
        self.assertEqual(sol.lastStoneWeight2(input), answer)
    def test2(self):
        sol = Solution()
        input = [1]
        answer = 1
        self.assertEqual(sol.lastStoneWeight2(input), answer)