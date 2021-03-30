"""
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

 

示例 1：

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.11.2 回溯，但是会超时
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def backtrace(n, cur):
            if cur == t:
                res[0] += 1
                return
            if n == len(s):
                return
            if t.startswith(cur):
                for i in range(n, len(s)):
                    backtrace(i+1, cur + s[i])
            
        res = [0]
        backtrace(0, '')
        return res[0]


# 2020.11.3 抄的别人的答案，坑爹的转移方程
class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s) +1) for _ in range(len(t)+1)]

        for i in range(len(s)+1):
            dp[0][i] = 1

        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]

# 2021.03.30 状态转移方程还是不会
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]
