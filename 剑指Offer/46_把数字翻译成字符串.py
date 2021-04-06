"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.06 自己做出来了
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        if not s: return 0
        if len(s) == 1: return 1
        dp = [0] * len(s)
        dp[0] = 1
        dp[1] += 1
        if 10<=int(s[0:2])<=25:
            dp[1] += 1
        for i in range(2, len(s)):
            dp[i] += dp[i-1]
            if 10<=int(s[i-1:i+1])<=25:
                dp[i] += dp[i-2]
        return dp[-1]


# 2021.04.06 民间大神解法
class Solution1:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a

class Solution2:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(len(s) - 2, -1, -1):
            a, b = (a + b if "10" <= s[i:i + 2] <= "25" else a), a
        return a


