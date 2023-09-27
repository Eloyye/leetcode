import unittest
from collections import Counter
from typing import List

class Solution:
    def delete_m(self, ids: List[int], m : int):
        count = Counter(ids)
        freq = sorted(count.values())
        deletions = 0
        for i in range(len(freq)):
            if deletions >= m:
                break
            while deletions < m and freq[i] > 0:
                freq[i] -= 1
                deletions += 1
        return sum(1 for f in freq if f > 0)
class DeleteTests(unittest.TestCase):
    def test1(self):
        sol = Solution()
        ans = ([1, 1, 1, 2, 3, 2], 2)
        res = sol.delete_m(ans[0], ans[1])
        expected = 2
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        ans = ([1, 2, 2, 3, 3, 3, 4], 3)
        res = sol.delete_m(ans[0], ans[1])
        expected = 2
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        ans = ([5, 7, 5, 5, 1, 2], 3)
        res = sol.delete_m(ans[0], ans[1])
        expected = 1
        self.assertEqual(expected, res)