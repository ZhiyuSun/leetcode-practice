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

# 2020.08.25
# 重温这道题，两个要点：1 用原数组；2 自下而上


# 2021.03.24 自己摸索出来了，一些边界条件处理不好
class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    if j == len(triangle[i]) - 1:
                        triangle[i][j] += triangle[i-1][j-1]
                    else:
                        triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

# 2021.03.24 自下而上会清楚很多
class Solution4:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]

# 2021.04.12 回答一个网友的问题，如何打印出路径
# 另外学到新知识：Python的内部函数，不修改全局变量可以访问全局变量
class Solution5:
    def __init__(self):
        self.max_value = float('inf')
        self.max_path = []

    def minimumTotalPath(self, triangle: List[List[int]]):
        def _dfs(level, s, path):
            if level == row:
                if s < self.max_value:
                    self.max_value = s
                    self.max_path = path
                return
            for i in triangle[level]:
                _dfs(level+1, s+i, path+[i])

        row = len(triangle)
        _dfs(0, 0, [])
        return self.max_path

# 2021.04.12 动态规划解法，需要额外开辟空间，不够简洁
class Solution6:
    def minimumTotalPath(self, triangle: List[List[int]]):
        path_arr = [[[]]*len(triangle[-1]) for _ in range(len(triangle))]
        for j in range(len(triangle[-1])):
            path_arr[-1][j] = [triangle[-1][j]]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                if triangle[i + 1][j] < triangle[i + 1][j + 1]:
                    path_arr[i][j] = [triangle[i][j]] + path_arr[i + 1][j]
                    triangle[i][j] += triangle[i + 1][j]
                else:
                    path_arr[i][j] = [triangle[i][j]] + path_arr[i + 1][j+1]
                    triangle[i][j] += triangle[i + 1][j + 1]
        return path_arr[0][0]