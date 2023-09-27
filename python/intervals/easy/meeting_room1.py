import unittest
from typing import List


class Solution:
    def can_attend_meetings(self, intervals: List[tuple[int, int]]) -> bool:
        intervals.sort()
        prev_end = float("-inf")
        for start, end in intervals:
            if prev_end <= start:
                prev_end = end
            else:
                return False
        return True

class MeetingRoomsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        intervals = [(0,30),(5,10),(15,20)]
        result = sol.can_attend_meetings(intervals)
        expected = False
        self.assertEqual(result, expected)
    def test2(self):
        sol = Solution()
        intervals = [(5,8),(9,15)]
        result = sol.can_attend_meetings(intervals)
        expected = True
        self.assertEqual(result, expected)
