"""
给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。

（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-common-supersequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.04.23 看不懂，直奔题解
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m = len(str1)
        n = len(str2)
        
        dp = [[''] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    if len(dp[i-1][j]) > len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
        
        i = 0
        j = 0
        lcs = dp[m][n]
        ans = ''
        for cur_char in lcs:
            while(i < m and str1[i] != cur_char):
                ans += str1[i]
                i += 1
            while(j < n and str2[j] != cur_char):
                ans += str2[j]
                j += 1
            
            ans += cur_char
            i += 1
            j += 1
        # 可能有尾部字符没有在LCS里，在这里加上
        return ans + str1[i:] + str2[j:]
