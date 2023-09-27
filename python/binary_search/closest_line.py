import unittest


class Solution:
    def find_closest_line(self, next_lines : list[int], offset: int) -> int:
        if not next_lines:
            return 1
        l, r = 0, len(next_lines) - 1
        while r > l:
            mid = (r + l) // 2
            if next_lines[mid] > offset:
                r = mid
            else:
                l = mid + 1
        return l

class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        next_lines = [13, 24, 38, 43]
        offset = 40
        res = sol.find_closest_line(next_lines, offset)
        expected = 3
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        next_lines = [13, 24, 30, 38, 43]
        offset = 27
        res = sol.find_closest_line(next_lines, offset)
        expected = 2
        self.assertEqual(expected, res)
