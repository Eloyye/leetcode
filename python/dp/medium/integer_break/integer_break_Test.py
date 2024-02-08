import unittest

from python.dp.medium.integer_break.integer_break import Solution2


class IntegerBreakTests(unittest.TestCase):
    def test1(self):
        integer_break = Solution2().integer_break
        n = 2
        res = integer_break(n)
        expect = 1
        self.assertEqual(expect, res)
    def test2(self):
        integer_break = Solution2().integer_break
        n = 10
        res = integer_break(n)
        expect = 36
        self.assertEqual(expect, res)

