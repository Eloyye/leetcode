from typing import List, Tuple


def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if grid is None:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited : set[Tuple[int,int]] = set()
    maxArea = 0

    def areaAt(row, col) -> int:
        isOutOfBounds = row < 0 or row >= rows or col < 0 or col >= cols
        isVisited = (row, col) in visited
        isOcean = grid[row][col] == 0 if not isOutOfBounds else False
        if isOutOfBounds or isVisited or isOcean:
            return 0
        visited.add((row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        totalArea = 0
        for dr, dc in directions:
            totalArea += areaAt(row + dr, col + dc)
        return totalArea + 1

    for row in range(rows):
        for col in range(cols):
            isLand = grid[row][col] == 1
            isNotVisited = (row, col) not in visited
            if isLand and isNotVisited:
                maxArea = max(areaAt(row, col), maxArea)
    return maxArea
