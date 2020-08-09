"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

"""
from typing import List

# 我的做法，居然成功了
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if i == 0:
                    if j > 0:
                        grid[i][j] += grid[i][j-1]
                elif j == 0:
                    if i > 0:
                        grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

# 官方解法+我的优化改进
class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        for i in range(1, rows): grid[i][0] += grid[i - 1][0]
        for j in range(1, columns): grid[0][j] += grid[0][j - 1]
        for i in range(1, rows):
            for j in range(1, columns):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]

