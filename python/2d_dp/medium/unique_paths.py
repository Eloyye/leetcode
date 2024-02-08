import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n + 1)]*(m + 1)
        dp[m - 1][n - 1] = 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        return dp[0][0]
    def uniquePathsLinear(self, m: int, n: int) -> int:
        prev_row = [1] * n
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1 , -1):
                prev_row[j] = new_row[j + 1] + prev_row[j]
            prev_row = new_row
        return prev_row[0]
class UniquePathsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        m, n = 3, 7
        result = sol.uniquePaths(m, n)
        expected = 28
        self.assertEqual(result, expected)