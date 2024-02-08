import unittest
from enum import Enum
from typing import List

class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable, atlantic_reachable = set(), set()

        def dfs(r, c, reachable_set, prev_height):
            if r < 0 or r > ROWS or c < 0 or c > COLS or (r, c) in reachable_set or heights[r][c] < prev_height:
                return
            reachable_set.add((r, c))
            directions = [(i, j) for i in [1, -1] for j in [1, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, reachable_set, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(ROWS - 1, c, pacific_reachable, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, atlantic_reachable, heights[r][0])
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r, c])
        return res


        ROWS, COLS = len(heights), len(heights[0])
        reachPacificSet, reachAtlanticSet = set(), set()
        # will this reach to both pacific and atlantic
        def dfs(r, c, visit, prevHeight):
            isOutOfBounds = r < 0 or r == ROWS or c < 0 or c == COLS
            alreadyVisited = (r,c) in visit
            isTooShortToFlow = heights[r][c] < prevHeight if not isOutOfBounds else False
            if isOutOfBounds or alreadyVisited or isTooShortToFlow:
                return
            visit.add((r,c))
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in direction:
                dfs(r + dr, c + dc, visit, heights[r][c])

        # First Row (Pacific) and the Last Row (Atlantic)
        for c in range(COLS):
            dfs(0, c, reachPacificSet, heights[0][c])
            dfs(ROWS - 1, c, reachAtlanticSet, heights[ROWS - 1][c])

        # First Column (pacific), last column (Atlantic)
        for r in range(ROWS):
            dfs(r, 0, reachPacificSet, heights[r][0])
            dfs(r, COLS - 1, reachAtlanticSet, heights[r][COLS - 1])

        #NOW AT THIS POINT WE HAVE MARKED ALL NODES THAT CAN REACH TO PACIFIC AND ATLANTIC, NOW
        # WE WANT THE UNION OF THIS SET
        # reachBoth = reachPacificSet & reachAtlanticSet
        # return list(reachBoth)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in reachPacificSet and (r,c) in reachAtlanticSet:
                    res.append([r, c])
        return res

class SolutionTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        res = sol.pacific_atlantic(input)
        expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        self.assertEqual(expected, res)
