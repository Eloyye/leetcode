import unittest
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_interval = {}
        for i, c in enumerate(s):
            if c not in char_to_interval:
                char_to_interval[c] = (i, i)
            else:
                char_to_interval[c] = (char_to_interval[c][0], i)
        intervals = list(char_to_interval.values())
        intervals.sort()
        merged_intervals = []
        for start, end in intervals:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])

        res = []
        for start, end in merged_intervals:
            res.append(end - start + 1)
        return res

class PartitionLabelsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s ="ababcbacadefegdehijhklij"
        res = sol.partitionLabels(s)
        expected = [9,7,8]
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        s = "eccbbbbdec"
        res = sol.partitionLabels(s)
        expected = [10]
        self.assertEqual(expected, res)