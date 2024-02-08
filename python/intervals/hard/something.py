import unittest


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        window = {}
        l = 0
        res = current = 0
        for i, c in enumerate(s):
            if c in window and l <= window[c]:
                l = window[c] + 1
                current = i - l + 1
            else:
                current += 1
            window[c] = i
            res = max(res, current)
        return res
class LTests(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "abcabcbb"
        res = sol.length_of_longest_substring(s)
        expected = 3
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        s = "bbbbb"
        res = sol.length_of_longest_substring(s)
        expected = 1
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        s = "pwwkew"
        res = sol.length_of_longest_substring(s)
        expected = 3
        self.assertEqual(expected, res)
