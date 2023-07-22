from collections import deque
from typing import List, Set, Any, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        # A set containing points that are represented as tuples (r, c)
        visited = set()
        islands = 0

        #bfs algo
        def bfs(r, c):
            #BFS -> requires queue
            #Priority queue containing tuples (r,c)
            q = deque()
            #add current point to visited
            visited.add((r,c))
            q.append((r,c))

            while q:
                #pop from FIFO
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                #navigate the neighbors of (row, col)
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    #make sure that the rows and columns are bounded
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r,c) not in visited:
                        q.append((r,c))
                        visited.add(r,c)

        # iterate through all
        for r in range(rows):
            for c in range(cols):
                #land
                if grid[r][c] == "1" and (r , c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            #base case if out of bounds, visited, or in ocean tile
            if (r not in range(rows)
            or c not in range(cols)
            or grid[r][c] == "0"
            or (r,c) in visited):
                return
            visited.add((r,c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        rows, columns = len(grid), len(grid[0])
        islands = 0
        visited: set[Tuple[int, int]] = set()
        def exploreIslandsAt(row : int, column :int) -> None:
            isOutOfBounds = row < 0 or row >= rows or column < 0 or column >= columns
            isVisited = (row, column) in visited
            isOcean = grid[row][column] == "0" if not isOutOfBounds else False
            if isOutOfBounds or isVisited or isOcean:
                return
            visited.add((row, column))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                exploreIslandsAt(row + dr, column + dc)

        for row in range(rows):
            for column in range(columns):
                isLand = grid[row][column] == "1"
                isNotVisited = (row, column) not in visited
                if isLand and isNotVisited:
                    islands += 1
                    exploreIslandsAt(row, column)
        return islands