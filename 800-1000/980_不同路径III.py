"""
在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

 

示例 1：

输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.18 掌握方法，困难题也不怕
class Solution:
    def __init__(self):
        self.res = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        count = 0
        row, col = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count += 1

        def _dfs(i, j):
            if grid[i][j] == 2:
                if len(visited) == count + 1:
                    self.res += 1
                return

            for m, n in direction:
                ni, nj = i + m, j + n
                if 0 <= ni < row and 0 <= nj < col:
                    if grid[ni][nj] in [0, 2] and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        _dfs(ni, nj)
                        visited.remove((ni, nj))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    _dfs(i, j)
        return self.res


# 2021.04.18 民间大神解法，清晰易懂
class Solution1:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.res = 0
        sr, sc = 0, 0                     #起点 终点
        er, ec = 0, 0
        step = 0                        #非障碍的个数
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:     sr, sc = r, c
                if grid[r][c] == 2:     er, ec = r, c
                if grid[r][c] != -1:    step += 1

        def dfs_backtrace(r, c, step):
            step -= 1
            if r == er and c == ec:
                if step == 0:
                    self.res += 1
                return
            grid[r][c] = -1
            for nr,nc in ((r-1,c),(r,c+1),(r+1,c),(r,c-1)):
                if 0<=nr<R and 0<=nc<C and grid[nr][nc] != -1:
                    dfs_backtrace(nr, nc, step)
            grid[r][c] = 0              #回溯算法
            
        dfs_backtrace(sr, sc, step)
        return self.res
