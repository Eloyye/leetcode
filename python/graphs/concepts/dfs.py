from typing import List


def dfs(grid: List[List[int]]):
    ROWS, COLS = len(grid), len(grid[0]),
    visit = set()
    def explore(i, j):
        if i < 0 or i > ROWS or j < 0 or j > COLS or (i, j) in visit or some_conditions:
            return
        visit.add((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            explore(i + dr, j + dc)
    for i in range(ROWS):
        for j in range(COLS):
            explore(i, j)
