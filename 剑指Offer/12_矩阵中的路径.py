"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.06 我自己写出来了！！！！
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def _dfs(i, j, cur):
            if cur == word:
                return True
            if not word.startswith(cur):
                return False
            visited.add((i, j))
            for m, n in directions:
                n_i = i + m
                n_j = j + n
                if 0 <= n_i < len(board) and 0 <= n_j < len(board[0]) and (n_i, n_j) not in visited:
                    resut = _dfs(n_i, n_j, cur+board[n_i][n_j])
                    if resut:
                        return True
            visited.remove((i, j))
            return False
            

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if _dfs(i, j, board[i][j]):
                    return True
        return False

# 2021.04.06 官方解法
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
