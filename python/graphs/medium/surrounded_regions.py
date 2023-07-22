from typing import List
import unittest

def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    ROWS, COLS = len(board), len(board[0])
    captured = set()

    def dfs(r, c, visited) -> bool:
        tileIsX = board[r][c] == "X"
        isVisited = (r, c) in visited
        isOnBorder = r < 1 or r >= (ROWS - 1) or c < 1 or c >= (COLS - 1)
        if tileIsX or isVisited:
            return True
        elif isOnBorder:
            return False
        visited.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        regionIsCaptured = True
        for dr, dc in directions:
            regionIsCaptured = regionIsCaptured and dfs(r + dr, c + dc, visited)
        return regionIsCaptured

    for r in range(ROWS):
        for c in range(COLS):
            tile = board[r][c]
            isNotInBorder = 0 < r < (ROWS - 1) and 0 < c < (COLS - 1)
            isO = tile == "O"
            isNotCaptured = (r, c) not in captured
            if isO and isNotInBorder and isNotCaptured:
                visited = set()
                if dfs(r, c, visited):
                    captured.update(visited)

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in captured:
                board[r][c] = "X"

def solve2(board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])
    # 1. Mark the unsurrounded O regions as non-capture ( O -> T)
    def capture(r, c):
        isOutOfBounds = r < 0 or r == ROWS or c < 0 or c == COLS
        isNotO = board[r][c] != "O" if not isOutOfBounds else False
        if isOutOfBounds or isNotO:
            return
        board[r][c] = "T"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            capture(r + dr, c + dc)

    for r in [0, ROWS - 1]:
        for c in range(COLS):
            isO = board[r][c] == "O"
            if isO:
                capture(r, c)

    for c in [0, COLS - 1]:
        for r in range(ROWS):
            isO = board[r][c] == "O"
            if isO:
                capture(r, c)

    # 2. Capture the surrounded regions
    for r in range(ROWS):
        for c in range(COLS):
            isO = board[r][c] == "O"
            if isO:
                board[r][c] = "X"
    # 3. Uncapture unsurrounded regions
    for r in range(ROWS):
        for c in range(COLS):
            isT = board[r][c] == "T"
            if isT:
                board[r][c] = "O"

class SurroundedRegionsTest(unittest.TestCase):
    def test1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]
        solve(board)
        self.assertEqual(board, expected)