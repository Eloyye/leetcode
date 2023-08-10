import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2),
        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
        return dp[ROWS][COLS]


class LCSTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        text1, text2 = "abcde", "ace",
        result = sol.longestCommonSubsequence(text1, text2)
        expected = 3
        self.assertEqual(result, expected)
    def test2(self):
        sol = Solution()
        text1, text2 = "abc", "def",
        result = sol.longestCommonSubsequence(text1, text2)
        expected = 0
        self.assertEqual(result, expected)