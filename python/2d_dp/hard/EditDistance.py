class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] := the minimum edit distance for transforming word1[i:] into word[j:]
        dp = [ [float("infinity") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # base case: bottom column
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        # base case: right column
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        #bottom-up dynamic programming
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    #no need to edit
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    #replace , insert, remove
                    insertion_cost = dp[i][j + 1]
                    deletion_cost = dp[i + 1][j]
                    replacement_cost = dp[i + 1][j + 1]
                    dp[i][j] = 1 + min(insertion_cost, deletion_cost, replacement_cost)
        return int(dp[0][0])

