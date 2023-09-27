import collections
from typing import List


def bfs(grid: List[List[int]]):
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    q = collections.deque()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # somehow q needs to be populated
    # initialization
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isNotVisited and isNotOutOfBounds and someOtherConditions:
                    q.append((nr, nc))
                    visited.add((nr, nc))


