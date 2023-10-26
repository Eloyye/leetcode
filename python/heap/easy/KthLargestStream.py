import unittest
from heapq import heapify
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
class KthLargestTest(unittest.TestCase):
    def test1(self):
        lg = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(lg.add(3), 4)
        self.assertEqual(lg.add(5), 5)
        self.assertEqual(lg.add(10), 5)
        self.assertEqual(lg.add(9), 8)
        self.assertEqual(lg.add(4), 8)



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)