"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

"""
from typing import List
# 我的解法
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if not n: return 0
        m = len(obstacleGrid[0])
        if not m: return 0
        dp = [[0]*m for _ in range(n)]
        for i in range(0, m):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1
        for j in range(0, n):
            if obstacleGrid[j][0] == 1: break
            dp[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# 别人的解法
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #新建矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])
        store = [[0]*width for i in range(height)]


        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if not obstacleGrid[m][n]: #如果这一格没有障碍物
                    if m == n == 0: #或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m-1][n] if m!=0 else 0 #上方格子
                        b = store[m][n-1] if n!=0 else 0 #左方格子
                        store[m][n] = a+b
        return store[-1][-1]