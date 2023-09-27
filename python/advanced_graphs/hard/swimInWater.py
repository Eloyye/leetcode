import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [(grid[0][0], (0, 0))]
        visit.add((0, 0))
        directions = [(1 , 0), (-1 ,0), (0, 1), (0, -1)]
        while minHeap:
            current_max_height, current_coordinate = heapq.heappop(minHeap)
            current_row, current_column = current_coordinate
            if current_row == n - 1 and current_column == n - 1:
                return current_max_height
            for dr, dc in directions:
                neighbor_row, neighbor_column = current_row + dr, current_column + dc
                isOutOfBounds = neighbor_row < 0 or neighbor_row >= n or neighbor_column < 0 or neighbor_column >= n
                if isOutOfBounds or (neighbor_row, neighbor_column) in visit:
                    continue
                visit.add((neighbor_row, neighbor_column))
                neighbor_max_height = max(current_max_height, grid[neighbor_row][neighbor_column])
                heapq.heappush(minHeap, (neighbor_max_height, (neighbor_row, neighbor_column)))