import functools
import unittest
from collections import deque
from typing import List, Deque


class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        def happyResult(n : int) -> bool:
            if n in visit:
                return False
            if n == 1:
                return True
            items = self.processIntToList(n)
            visit.add(n)
            result = 0
            for it in items:
                result += it**2
            return happyResult(result)
        return happyResult(n)
    def processIntToList(self, num : int) -> List[int]:
        res = []
        while num > 0:
            digit = num % 10
            res.append(digit)
            num = num // 10
        return res

class IsHappyTest(unittest.TestCase):
    tests = [19, 2]
    ans = [True, False]
    def test_unit_isHappy(self):
        sol = Solution()
        for i in range(len(self.tests)):
            self.assertEqual(self.ans[i], sol.isHappy(self.tests[i]))
    def test_unit_isHappy(self):
        sol = Solution()
        print(sol.processIntToList(10))