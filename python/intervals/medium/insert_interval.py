import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

class InsertIntervalTest(unittest.TestCase):
    sol = Solution()
    def test1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        out = self.sol.insert(intervals, newInterval)
        expected = [[1,5],[6,9]]
        self.assertEqual(out, expected)
    def test2(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        out = self.sol.insert(intervals, newInterval)
        expected = [[1,5],[6,9]]
        self.assertEqual(out, expected)