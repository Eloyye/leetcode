from enum import Enum
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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