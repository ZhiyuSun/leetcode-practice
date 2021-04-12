"""
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
示例 :

X..X
...X
...X
在上面的甲板中有2艘战舰。

无效样例 :

...X
XXXX
...X

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/battleships-in-a-board
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.12 我的解法，DFS
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return 0
        row = len(board)
        col = len(board[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def _dfs(i, j):
            board[i][j] = '.'
            for m, n in direction:
                n_i, n_j = i+m, j+n
                if 0<=n_i<row and 0<=n_j<col and board[n_i][n_j] == 'X':
                    _dfs(n_i, n_j)

        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    count += 1
                    _dfs(i, j)
        return count

# 2021.04.12 民间解法，因为战舰的特殊性，其实不需要DFS
class Solution1:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        res =  0
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".": continue
                if i > 0 and board[i - 1][j] == "X": continue
                if j > 0 and board[i][j - 1] == "X": continue
                res += 1
        return res
