from collections import defaultdict
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set) # key: tuple (r// 3, c // 3)
    for r in range(len(board)):
        for c in range(len(board[0])):
            # don't really care if empty, only filled
            if board[r][c] == '.':
                continue
            #check for duplicate -> false if so
            if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True