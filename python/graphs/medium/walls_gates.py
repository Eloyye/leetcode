from collections import deque
from typing import List
import unittest


def add_rooms(visited, q, ROWS, COLS, rooms, r, c):
    if (r < 0 or r >= ROWS or c < 0 or c >= COLS) or (r, c) in visited or rooms[r][c] == -1:
        return visited, q
    visited.add((r, c))
    q.append((r, c))
    return visited, q

class Solution:
    def walls_and_gates2(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0]),
        visited = set()
        q = deque()
        distance = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # get all the gates
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = distance
                for dr, dc in directions:
                    visited, q = add_rooms(visited, q, ROWS, COLS, rooms, r + dr, c + dc)
            distance += 1
    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def addRooms(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS) or (r, c) in visited or rooms[r][c] == -1:
                return
            q.append((r,c))
            visited.add((r,c))

        # 1. Get all the gates
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        distance = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = distance
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    addRooms(r + dr, c + dc)
            distance += 1

def print2D(grid):
    print('\n \n')
    for r in grid:
        print(r)
class WallsGatesTest(unittest.TestCase):
    def test1(self):
        rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        answer = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
        walls_and_gates = Solution().walls_and_gates2
        walls_and_gates(rooms)
        print2D(answer)
        print2D(rooms)
        self.assertEqual(rooms, answer)
    def test2(self):
        rooms = [[0,-1],[2147483647,2147483647]]
        answer = [[0,-1],[1,2]]
        walls_and_gates = Solution().walls_and_gates2
        walls_and_gates(rooms)
        self.assertEqual(rooms, answer)
