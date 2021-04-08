"""
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
"""

# 2021.04.08 我居然做出来了
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]




# s[i] = s[j]:
# dp[i][j] = dp[i+1][j-1] + 2
# s[i] != s[j]:
# dp[i][j] = max(dp[i+1][j], dp[i][j-1])

#    b  b  b  a  b  j
# b  1  2  3  3  4
# b  x  1  2  2  3
# b  x  x  1  1  3 
# a  x  x  x  1  1 
# b  x  x  x  x  1  

# i





