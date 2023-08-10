import unittest
from collections import defaultdict
from typing import List


class Solution:
    ##
    # Given an m x n integers matrix, return the length of the longest increasing path in matrix.
    # From each cell, you can either move in four directions: left, right, up, or down.
    # You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
    #
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0]),
        dp = {}
        LIP = 0

        def dfs(i ,j, prev_value):
            isOutOfBounds = i < 0 or i >= ROWS or j < 0 or j >= COLS
            current_value = matrix[i][j] if not isOutOfBounds else -1
            if isOutOfBounds and prev_value >= current_value:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            cur_len = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                cur_len = max(cur_len, dfs(i + dr, j + dc, current_value))
            dp[(i, j)] = cur_len
            return cur_len
        for i in range(ROWS):
            for j in range(COLS):
                LIP = max(LIP, dfs(i, j, -1))
        return LIP


class longestIncreasingPathTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        matrix = [[9,9,4],[6,6,8],[2,1,1]]
        result = sol.longestIncreasingPath(matrix)
        expected = 4
        self.assertEqual(expected, result)
    def test2(self):
        sol = Solution()
        matrix = [[7,7,5],[2,4,6],[8,2,0]]
        result = sol.longestIncreasingPath(matrix)
        expected = 4
        self.assertEqual(expected, result)

