import unittest


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_size, t_size = len(s), len(t),
        dp = [[0 for _ in range(t_size + 1)] for _ in range(s_size + 1)]
        for i in range(s_size + 1):
            dp[i][t_size] = 1
        for i in range(s_size - 1, -1, -1):
            for j in range(t_size - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]

class NumDistinctTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "rabbbit"
        t = "rabbit"
        result = sol.numDistinct(s, t)
        expected = 3
        self.assertEqual(expected, result)
    def test2(self):
        sol = Solution()
        s = "babgbag"
        t = "bag"
        result = sol.numDistinct(s, t)
        expected = 5
        self.assertEqual(expected, result)