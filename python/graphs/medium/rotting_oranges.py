from collections import deque
from typing import List
import unittest

def orangesRotting(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0]),
    visited = set()
    q = deque()
    timeElapsed = 0
    for r in range(ROWS):
        for c in range(COLS):
            isRottingOrange = grid[r][c] == 2
            if isRottingOrange:
                visited.add((r, c))
                q.append((r, c))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        # process all nodes in the queue (this constitutes a single "minute")
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                isNewPointInBounds = (0 <= new_r < ROWS) and (0 <= new_c < COLS)
                isNewPointFresh = grid[new_r][new_c] == 1 if isNewPointInBounds else False
                isNotVisited = (new_r, new_c) not in visited
                if isNewPointInBounds and isNewPointFresh and isNotVisited:
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))
                    grid[new_r][new_c] = 2  # Mark the fresh orange as rotten
        if q:
            timeElapsed += 1
    # Check if there are still fresh oranges left
    if any(1 in row for row in grid):
        return -1
    return timeElapsed
class RottingOrangesTest(unittest.TestCase):
    def test1(self):
        grid = [
            [2,1,1],
            [1,1,0],
            [0,1,1]
        ]
        expected = 4
        self.assertEqual(orangesRotting(grid), expected)
    def test2(self):
        grid = [
            [2,1,1],
            [0,1,1],
            [1,0,1]
        ]
        expected = -1
        self.assertEqual(orangesRotting(grid), expected)