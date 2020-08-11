"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]


        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]
        
        return min(f)


# 我的错误解法
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def _dfs(i, j, amount, min_amount):
            if i == len(triangle):
                return min_amount if amount > min_amount else amount
            amount += triangle[i][j]
            min_result1 = _dfs(i+1, j, amount, min_amount)
            amount -= triangle[i][j]
            amount += triangle[i][j]
            min_result2 = _dfs(i+1, j+1, amount, min_amount)
            amount -= triangle[i][j]
            return min(min_result1, min_result2, min_amount)
        return _dfs(0, 0, 0, float('inf'))

# 动态规划
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]