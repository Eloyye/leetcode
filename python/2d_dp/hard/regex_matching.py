class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        n, m = len(s), len(p)
        def isMatchStarting(i, j):
            if (i , j) in memo:
                return memo[(i, j)]
            elif i >= n and j >= m:
                return True
            elif j >= m:
                return False
            charMatches = i < n and (s[i] == p[j] or (p[j] == "."))
            isAsteriskAhead = (j + 1) < m and p[j + 1] == "*"
            if isAsteriskAhead:
                skipAsterick = isMatchStarting(i, j + 2)
                useAsterick = charMatches and isMatchStarting(i + 1, j)
                memo[(i, j)] = skipAsterick or useAsterick
                return memo[(i, j)]
            elif charMatches:
                memo[(i, j)] = isMatchStarting(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False

        return isMatchStarting(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}
        def dfs(i : int, j : int) -> bool:
            currentPosition = (i, j)
            if currentPosition in memo:
                return memo[currentPosition]
            if i >= n and j >= m:
                return True
            if j >= m:
                return False
            match = i < n and (s[i] == p[j] or p[j] == ".")
            isAstericksAhead = (j + 1) < m and p[j + 1] == "*"
            if isAstericksAhead:
                skipAstericks, useAstericks = dfs(i, j + 2), match and dfs(i + 1, j)
                memo[currentPosition] = skipAstericks or useAstericks
                return memo[currentPosition]
            if match:
                memo[currentPosition] = dfs(i + 1, j + 1)
                return memo[currentPosition]
            memo[currentPosition] = False
            return False
        return dfs(0, 0)