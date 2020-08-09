"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _dfs(i, j):
            if i < 0 or j < 0 or i >= m or j>= n or grid[i][j] == '0': 
                return 
            grid[i][j] = '0'
            _dfs(i, j+1)
            _dfs(i, j-1)
            _dfs(i+1, j)
            _dfs(i-1 , j)

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        count = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    count += 1
                    _dfs(i, j)
        return count

# BFS
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        count = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    queue = [(i, j)]
                    while queue:
                        row, col = queue.pop(0)
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                                queue.append((x, y))
                                grid[x][y] = "0"
        return count

# 并查集的方法, 需要好好理解
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)
        
        return uf.getCount()
