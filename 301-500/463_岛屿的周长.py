"""
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/island-perimeter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.10.31 直奔题解的一天，dfs
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def _dfs(x, y, grid, n, m):
            if  x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0
            grid[x][y] = 2
            res = 0
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                res += _dfs(tx, ty, grid, n, m) 
            return res
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += _dfs(i, j, grid, n, m)
        return ans


# 2021.04.13 完全用数学法给做出来了
class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 4
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < row and 0 <= nj < col:
                            if grid[ni][nj] == 1:
                                count -= 1
        return count
