import unittest
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        current = []
        removals = 0
        for low, high in intervals:
            if not current or current[-1][1] <= low:
                current.append([low, high])
            else:
                removals += 1
                if current[-1][1] > high:
                    current.pop()
                    current.append([low, high])
        return removals

    def eraseOverlapIntervals_ending_time(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals, prev_end = 0, float('-inf')
        for low, high in intervals:
            if prev_end <= low:
                #no overlap
                prev_end = high
            else:
                #overlap
                removals += 1
        return removals

class EraseOverlapIntervalsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        inp = [[1,2],[2,3],[3,4],[1,3]]
        res = sol.eraseOverlapIntervals(inp)
        expect = 1
        self.assertEqual(expect, res)
    def test2(self):
        sol = Solution()
        inp = [[1,2],[1,2],[1,2]]
        res = sol.eraseOverlapIntervals(inp)
        expect = 2
        self.assertEqual(expect, res)
    def test3(self):
        sol = Solution()
        inp = [[1,2],[2,3]]
        res = sol.eraseOverlapIntervals(inp)
        expect = 0
        self.assertEqual(expect, res)