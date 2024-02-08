from typing import List, Tuple


class MaxAreaSolution:
    def max_area_of_island(self, grid: list[list[int]]) -> int:
        if grid is None:
            return 0
        ROWS, COLS = len(grid), len(grid[0]),
        # set of (row : int, col : int)
        visited : set[tuple[int, int]] = set()
        max_area = 0

        def area_at(r, c) -> int:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            directions = [(i , j) for i in [-1, 1] for j in [-1, 1]]
            area = 1
            for dr, dc in directions:
                area += area_at(r + dr, c + dc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, area_at(r, c))
        return max_area
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
