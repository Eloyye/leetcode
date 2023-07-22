import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

class FindKthLargestTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        input = [3,2,1,5,6,4]
        k = 2
        expected = 5
        self.assertEqual(sol.findKthLargest(input, k), expected)
    def test2(self):
        sol = Solution()
        input = [3,2,3,1,2,4,5,5,6]
        k = 4
        expected = 4
        self.assertEqual(sol.findKthLargest(input, k), expected)