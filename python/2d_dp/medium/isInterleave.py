import unittest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                elif j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
class IsInterleave(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        result = sol.isInterleave(s1,s2,s3)
        self.assertTrue(result)
    def test2(self):
        sol = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        result = sol.isInterleave(s1,s2,s3)
        self.assertFalse(result)
    def test3(self):
        sol = Solution()
        s1 = ""
        s2 = ""
        s3 = ""
        result = sol.isInterleave(s1,s2,s3)
        self.assertTrue(result)
