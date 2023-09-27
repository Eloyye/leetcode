import unittest
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        prev_high = float('-inf')
        longest_chain = 0
        for current_low, current_high in pairs:
            if current_low > prev_high:
                longest_chain += 1
                prev_high = current_high
        return longest_chain

class FindLongestChainTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        pairs = [[1,2],[2,3],[3,4]]
        res = sol.findLongestChain(pairs)
        expected = 2
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        pairs = [[1,2],[7,8],[4,5]]
        res = sol.findLongestChain(pairs)
        expected = 3
        self.assertEqual(expected, res)