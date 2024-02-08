from collections import deque
from typing import List
import unittest


class RottingOrangesSolution:
    def oranges_rotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        time_elapsed = 0

        def insert_rotten_oranges(visited):
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r, c))
            return visited

        visited = insert_rotten_oranges(visited)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))
                grid[r][c] = 2
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                # when processing the neighbors, the only responsibility is adding to queue/deque
                # This is the relaxation step
                for dr, dc in directions:
                    r += dr
                    c += dc
                    if (0 <= r < ROWS and 0 <= c < COLS) and ((r, c) not in visited) and grid[r][c] == 1:
                        q.append((r, c))
            if q:
                time_elapsed += 1
        return time_elapsed if not any(1 in row for row in grid) else -1


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
