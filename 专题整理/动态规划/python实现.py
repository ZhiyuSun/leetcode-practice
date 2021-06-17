from typing import List
# 300. 最长上升子序列
class Solution300:

    # 贪心+二分
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)

    # 动态规划
    def lengthOfLIS1(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

# 673. 最长递增子序列的个数
class Solution673:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1

        dp = [1] * n
        count = [1] * n
        max_length = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            max_length = max(max_length, dp[i])

        res = 0
        for i in range(n):
            if dp[i] == max_length:
                res += count[i]
        return res
# 53. 最大子序和
class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)

# 198. 打家劫舍
class Solution198:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second

# 213. 打家劫舍 II
class Solution213:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

# 91. 解码方法
class Solution91:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        # 考虑第一个字母
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1: return dp[-1]
        # 考虑第二个字母
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            # 当出现连续两个0
            if s[i - 1] + s[i] == "00": return 0
            # 考虑单个字母
            if s[i] != "0":
                dp[i] += dp[i - 1]
                if 10 <= int(s[i - 1] + s[i]) <= 26:
                    dp[i] += dp[i - 2]
            # 考虑两个字母
            else:
                if 1 <= int(s[i-1]) <= 2:
                     dp[i] += dp[i - 2]
                else:
                    return 0
        return dp[-1]

# 62. 不同路径
class Solution62:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m]
        for _ in range(n-1):
            dp.append([1] + [0] * (m-1))
        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = dp[j-1][i] + dp[j][i-1] 

        return dp[-1][-1]

# 63. 不同路径 II
class Solution63:
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

# 980. 不同路径 III
class Solution980:
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

# 72. 编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row, col = len(word1)+1, len(word2)+1
        dp = [[0] * col for _ in range(row)]
        for i in range(0, row):
            dp[i][0] = i
        for j in range(0, col):
            dp[0][j] = j
        for i in range(1, row):
            for j in range(1, col):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
