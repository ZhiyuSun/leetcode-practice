"""
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

 

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


# 2021.03.17 复习巩固，理解上有难度
class Solution1:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

# https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zi-xu-lie-wen-ti-tong-yong-si-lu-zui-chang-hui-wen/
# 拉布拉东的题解很好，要注意采用反向遍历，因为dp[i][j]依赖于dp[i+1][j-1],dp[i+1]dp[j],dp[i][j-1]三个值

# 2021.03.30 这比最长回文子串难多了，yyds
class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

# 这状态转移方程也太难了
# if (s[i] == s[j])
#     // 它俩一定在最长回文子序列中
#     dp[i][j] = dp[i + 1][j - 1] + 2;
# else
#     // s[i+1..j] 和 s[i..j-1] 谁的回文子序列更长？
#     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);


# 2021.04.08 我自己做出来了，666
class Solution3:
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





