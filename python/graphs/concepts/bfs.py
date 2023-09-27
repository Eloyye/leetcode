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
                if ((nr, nc) not in visited) and ( 0 <= nr <= ROWS - 1 and 0 <= nc <= COLS - 1 ) and someOtherConditions:
                    q.append((nr, nc))
                    visited.add((nr, nc))


