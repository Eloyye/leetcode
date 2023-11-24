import unittest


def dfs(i, j, n, board, visit, x_placed, o_placed) -> int:
    if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visit:
        return 0
    # resolve the following vars
    if x_wins_state or o_wins_state or draw_state:
        return 1
    else:
        visit.add((i, j))
        valid_combs = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if x_placed == o_placed:
            symbol = "o"
            new_x_placed = x_placed
            new_o_placed = o_placed + 1
            num_tries = 2
        elif x_placed > o_placed:
            symbol = "o"
            new_x_placed = x_placed
            new_o_placed = o_placed + 1
            num_tries = 1
        else:
            symbol = "x"
            new_x_placed = x_placed + 1
            new_o_placed = o_placed
            num_tries = 1
        while num_tries > 0:
            board[i][j] = symbol
            for dr, dc in directions:
                valid_combs += dfs(i + dr, j + dc, n, board, visit, new_x_placed, new_o_placed)
            board[i][j] = None
            symbol = 'o' if symbol == 'x' else 'o'
            new_x_placed = new_x_placed - 1 if symbol == 'x' else new_x_placed
            new_o_placed = new_o_placed - 1 if symbol == 'o' else new_o_placed
        return valid_combs

class Solution:
    def resolve_ttt(self, n : int) -> int:
        board = [[None]* n] * n
        valid_combs = 0
        visit = set()
        _, valid_combs, _ = dfs(0, 0, n, board, visit, 0, 0)
        return valid_combs

class TicTacToeTests(unittest.TestCase):
    def test1(self):
        resolve_ttt = Solution().resolve_ttt
        res = resolve_ttt(3)
        # print(res)