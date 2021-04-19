"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j]: ans += 1
        return ans
# 2021.03.17 这种方法太绕了，不学也罢


# 2021.03.17 中心扩散法
class Solution2:
    def __init__(self):
        self.count = 0

    def countSubstrings(self, s: str) -> int:
        size = len(s)
        if size < 2: return size
        for i in range(size):
            self.center_spread(s, size, i, i)
            self.center_spread(s, size, i, i + 1)
        return self.count

    def center_spread(self, s, size, left, right):
        i = left
        j = right
        while i>=0 and j<size and s[i]==s[j]:
            i-=1
            j+=1
            self.count+=1

# 2021.03.17 新的动态规划法
class Solution3:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(0, j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1
        return ans

# 状态：dp[i][j] 表示字符串s在[i,j]区间的子串是否是一个回文串。
# 状态转移方程：当 s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1]) 时，dp[i][j]=true，否则为false


# 2021.03.30 还是不会，要特别注意一下了


# 2021.03.30 中心扩散法yyds
class Solution4:
    def __init__(self):
        self.count = 0

    def countSubstrings(self, s: str) -> int:
        size = len(s)
        if size < 2: return size
        for i in range(size):
            self.center_spread(s, size, i, i)
            self.center_spread(s, size, i, i + 1)
        return self.count

    def center_spread(self, s, size, left, right):
        i = left
        j = right
        while i>=0 and j<size and s[i]==s[j]:
            i-=1
            j+=1
            self.count+=1

# 2021.03.30 重温动态规划法，s[i][j]代表从i到j的截取后的字符串
class Solution5:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(0, j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1
        return ans

# 2021.04.19 这题居然还是不会，dp[i][j]可代表从i到j截取后的字符串
class Solution6:
    def countSubstrings(self, s: str) -> int:        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(0, j+1):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1
        return ans
