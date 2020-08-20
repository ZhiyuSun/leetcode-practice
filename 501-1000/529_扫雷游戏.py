"""
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。
 

示例 1：

输入: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

"""
from typing import List
# 2020.08.20 继续直奔题解
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dir_x = [0, 1, 0, -1, 1, 1, -1, -1]
        dir_y = [1, 0, -1, 0, 1, -1, 1, -1]

        def dfs(board, x, y):
            count = 0
            for i in range(0, 8):
                tx = x + dir_x[i]
                ty = y + dir_y[i]
                if tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0]):
                    continue
                if board[tx][ty] == 'M':
                    count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for i in range(0, 8):
                    tx = x + dir_x[i]
                    ty = y + dir_y[i]
                    if tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0]) or board[tx][ty] != 'E':
                        continue
                    dfs(board, tx, ty)

        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(board, x, y)
        return board


# 超哥版,绝了
class Solution1:
    def updateBoard(self, board, click):
        row, col = click[0], click[1]
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row + r][col + c] == 'M' for r, c in dirs if 0 <= row + r < len(board) and 0 <= col + c < len(board[0])])
                board[row][col] = n and str(n) or 'B'
                for r, c in dirs * (not n): 
                    self.updateBoard(board, [row + r, col + c])
        return board