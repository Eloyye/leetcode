import unittest
from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        # prefer the input `digits` be a deque data structure
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            if digit == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                carry = False
                break
        if carry:
            digits.insert(0, 1)
        return digits

class PlusOneTest(unittest.TestCase):
    test_case = [[1,2,3], [4,3,2,1], [9], [8,9,9,9]]
    solution_case = [[1,2,4], [4,3,2,2], [1,0], [9,0,0,0]]
    def test1(self):
        sol = Solution()
        digits = self.test_case[0]
        res = sol.plusOne(digits)
        expected = self.solution_case[0]
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        digits = self.test_case[1]
        res = sol.plusOne(digits)
        expected = self.solution_case[1]
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        digits = self.test_case[2]
        res = sol.plusOne(digits)
        expected = self.solution_case[2]
        self.assertEqual(expected, res)
    def test4(self):
        sol = Solution()
        digits = self.test_case[3]
        res = sol.plusOne(digits)
        expected = self.solution_case[3]
        self.assertEqual(expected, res)
    def test_all(self):
        sol = Solution()
        for i in range(len(self.test_case)):
            digits = self.test_case[i]
            res = sol.plusOne(digits)
            expected = self.solution_case[i]
            self.assertEqual(expected, res)

