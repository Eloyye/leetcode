import unittest
from collections import deque


class Solution:
    def parse_int(self, num1_str: str) -> int:
        res = 0
        n = len(num1_str)
        for i in range(n, 0, -1):
            num_ = ord(num1_str[i - 1]) - ord("0")
            res += num_ * 10 ** (n - i)
        return res

    def to_string(self, n: int) -> str:
        if n == 0:
            return "0"
        res = deque()
        while n:
            res.appendleft(chr(n % 10 + ord("0")))
            n = n // 10
        return "".join(res)
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = self.parse_int(num1), self.parse_int(num2)
        return self.to_string(n1 * n2)

class MultiplyTest(unittest.TestCase):
    def test_parse_int(self):
        sol = Solution()
        num1, num2 = "2", "3"
        n1, n2 = sol.parse_int(num1), sol.parse_int(num2)
        self.assertEqual(n1, 2)
        self.assertEqual(n2, 3)
    def test_to_string(self):
        sol = Solution()
        res = sol.to_string(321)
        expected = "321"
        self.assertEqual(expected, res)
    def test_whole_1(self):
        sol = Solution()
        num1, num2 = "2", "3"
        res = sol.multiply(num1, num2)
        expected = "6"
        self.assertEqual(res, expected)
    def test_whole_2(self):
        sol = Solution()
        num1, num2 = "123", "456"
        res = sol.multiply(num1, num2)
        expected = "56088"
        self.assertEqual(res, expected)
    def test_whole_3(self):
        sol = Solution()
        num1, num2 = "0", "0"
        res = sol.multiply(num1, num2)
        expected = "0"
        self.assertEqual(res, expected)