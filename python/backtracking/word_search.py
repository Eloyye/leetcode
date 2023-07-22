from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    #len of rows and cols of board
    rows, cols = len(board), len(board[0])

    # starting at position (i, j) and first k values are correct for word,
    # does it form word after k + 1?
    def dfs(i: int, j: int, k: int) -> bool:
        #success case
        if k == len(word):
            return True
        # failure case: out of bounds, current value of board does not match corresponding index of word
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
            return False
        # prevent the case where you are including adjacent characters that you have already included
        temp, board[i][j] = board[i][j], '/'
        # current value does match
        found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            # can you form `word` starting at (i, j)
            if dfs(i, j, 0):
                return True
    #otherwise no luck
    return False