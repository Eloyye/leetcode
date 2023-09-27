import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        while n:
            num_ones += n & 1
            n = n >> 1
        return num_ones

class HammingWeightTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        res = sol.hammingWeight(0o0000000000000000000000000001011)
        expected = 3
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        res = sol.hammingWeight(0o00000000000000000000000010000000)
        expected = 1
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        res = sol.hammingWeight(0o11111111111111111111111111111101)
        expected = 31
        self.assertEqual(expected, res)
