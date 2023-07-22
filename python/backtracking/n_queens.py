from typing import List, Set, Any


def solveNQueens(n: int) -> List[List[str]]:
    # we want to keep track of columns, positive-sloped diagonals, negative-sloped diagonals in which the
    # queens are placed
    col, posDiag, negDiag = set(), set(), set()
    res = []
    # nxn board, . indicates empty tile
    board = [["."] * n for _ in range(n)]

    # backtrack through all the rows
    def bt(r: int):
        if r == n:
            # result should be in the format of string
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        # iterate through all the columns
        for c in range(n):
            # check whether there is a queen on the column or diagonals
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            # add to board and to the set
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"
            bt(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    bt(0)
    return res

#verbose
def solveNQueens2(n: int) -> List[List[str]]:
    result: List[List[str]] = []
    queen_in_column, queen_in_positive_diagonal, queen_in_negative_diagonal = set(), set(), set()
    boardNxN: list[list[str]] = [["."] * n for _ in range(n)]

    def backtrack_rows(row: int) -> None:
        if row == n:
            # each row could be represented as ["Q...", "...Q", ...]
            copy = ["".join(_row) for _row in boardNxN]
            result.append(copy)
            return
        for column in range(n):
            if column in queen_in_column or (row - column) in queen_in_negative_diagonal or (
                    row + column) in queen_in_positive_diagonal:
                continue
            queen_in_column.add(column)
            queen_in_positive_diagonal.add(row + column)
            queen_in_negative_diagonal.add(row - column)
            boardNxN[row][column] = 'Q'
            backtrack_rows(row + 1)
            queen_in_column.remove(column)
            queen_in_positive_diagonal.remove(row + column)
            queen_in_negative_diagonal.remove(row - column)
            boardNxN[row][column] = '.'
    backtrack_rows(0)
    return result
