import unittest
from typing import List


class Solution:
    def mergeAttempt(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for interval in intervals:
            for placed_intervals in res:
                isDisjoint = (placed_intervals[1] < interval[0] and placed_intervals[1] < interval[1]) or \
                                   (placed_intervals[0] > interval[1] and placed_intervals[0] > interval[0])
                if isDisjoint:
                    res.append(interval)
                    break
                else:
                    placed_intervals[0] = min(placed_intervals[0], interval[0])
                    placed_intervals[1] = max(placed_intervals[1], interval[1])
                    break
            if not res:
                res.append(interval)
        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        

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