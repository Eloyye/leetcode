import unittest
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        pairs = 0
        for n in nums:
            if n in seen:
                pairs += seen[n]
                seen[n] += 1
            else:
                seen[n] = 1
        return pairs

class NumIdentPairsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        nums = [1,2,3,1,1,3]
        res = sol.numIdenticalPairs(nums)
        expected = 4
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        nums = [1,1,1,1]
        res = sol.numIdenticalPairs(nums)
        expected = 6
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        nums = [1,2,3]
        res = sol.numIdenticalPairs(nums)
        expected = 0
        self.assertEqual(expected, res)