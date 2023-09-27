import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for low, high in intervals:
            if not res or res[-1][1] < low:
                #disjoint or beginning
                res.append([low, high])
            else:
                #merge
                res[-1][1] = max(high, res[-1][1])
        return res

class MergeIntervalsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        result = sol.merge(intervals)
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(result, expected)
    def test2(self):
        sol = Solution()
        intervals = [[1,4],[4,5]]
        result = sol.merge(intervals)
        expected = [[1,5]]
        self.assertEqual(result, expected)
    def test3(self):
        sol = Solution()
        intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
        result = sol.merge(intervals)
        expected = [[1,10]]
        self.assertEqual(result, expected)