from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def _dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] in ['X', '#']: return
            board[i][j] = '#'
            _dfs(i-1, j)
            _dfs(i+1, j)
            _dfs(i, j-1)
            _dfs(i, j+1)

        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                is_edge = i == 0 or j == 0 or i == m-1 or j == n-1
                if is_edge and board[i][j] == 'O':
                    _dfs(i, j)
        print(board)

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
