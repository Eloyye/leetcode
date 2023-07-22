import unittest
from heapq import heapify
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapify(self.minHeap)
        # We are doing this so that the size of the min heap is K
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # could be that the heap is of size less than k, then that means we don't want to pop
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
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