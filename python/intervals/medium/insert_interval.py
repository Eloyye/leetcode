import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, current_interval in enumerate(intervals):
            if newInterval[1] < current_interval[0]:
                # ...............[current_interval]
                # [new_interval]
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > current_interval[1]:
                # [current_interval]...............[next_interval]
                # ..................[new_interval]
                result.append(current_interval)
            else:
                # Overlapping
                # .......[current_interval]
                # [new_interval]
                newInterval = [min(newInterval[0], current_interval[0]), max(newInterval[1], current_interval[1])]
        #consider the case where [last_interval_from_list] [new_interval]
        result.append(newInterval)
        return result
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