import unittest
from typing import List


class Solution:
    def min_meeting_rooms(self, intervals: List[tuple[int,int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        rooms, prev_end = 1, float("-inf")
        for current_start, current_end in intervals:
            if prev_end <= current_start:
                prev_end = current_end
            else:
                rooms += 1
        return rooms


class MeetingRooms2Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        intervals = [(0,30),(5,10),(15,20)]
        res = sol.min_meeting_rooms(intervals)
        expected = 2
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        intervals = [(2,7)]
        res = sol.min_meeting_rooms(intervals)
        expected = 1
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        intervals = [(1,5),(8,9),(8,9)]
        res = sol.min_meeting_rooms(intervals)
        expected = 2
        self.assertEqual(expected, res)
    def test4(self):
        sol = Solution()
        intervals = [(1,5),(8,9),(8,9),(2,7)]
        res = sol.min_meeting_rooms(intervals)
        expected = 3
        self.assertEqual(expected, res)
    def test5(self):
        sol = Solution()
        intervals = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
        res = sol.min_meeting_rooms(intervals)
        expected = 3
        self.assertEqual(expected, res)
    def test6(self):
        sol = Solution()
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        intervals = [(start, end) for start,end in intervals]
        res = sol.min_meeting_rooms(intervals)
        expected = 4
        self.assertEqual(expected, res)

