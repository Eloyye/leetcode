import unittest
from typing import List

class Solution:
    def Solution(self):
        ...
    def rob(self, nums: List[int]) -> int:
        return max(max(self.robHelper(nums[:len(nums) - 1]), self.robHelper(nums[1:])), nums[0])
    def robHelper(self, nums):
        rob1 = rob2 = 0
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)
        return rob2

class RobTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        inp = [2, 3, 2]
        out = 3
        self.assertEqual(sol.rob(inp), out)
    def test2(self):
        sol = Solution()
        inp = [1,2,3,1]
        out = 4
        self.assertEqual(sol.rob(inp), out)
    def test3(self):
        sol = Solution()
        inp = [1]
        out = 1
        self.assertEqual(sol.rob(inp), out)