"""
在一个大小在 (0, 0) 到 (N-1, N-1) 的2D网格 grid 中，除了在 mines 中给出的单元为 0，其他每个单元都是 1。网格中包含 1 的最大的轴对齐加号标志是多少阶？返回加号标志的阶数。如果未找到加号标志，则返回 0。

一个 k" 阶由 1 组成的“轴对称”加号标志具有中心网格  grid[x][y] = 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。下面给出 k" 阶“轴对称”加号标志的示例。注意，只有加号标志的所有网格要求为 1，别的网格可能为 0 也可能为 1。

 

k 阶轴对称加号标志示例:

阶 1:
000
010
000

阶 2:
00000
00100
01110
00100
00000

阶 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-plus-sign
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.17 直奔题解，看不懂解法
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0
        
        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0
            for c in range(N-1, -1, -1):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in range(N-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
        
        return ans

