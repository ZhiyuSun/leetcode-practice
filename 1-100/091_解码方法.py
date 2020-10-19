"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

"""
from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1: return dp[-1]
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            if s[i - 1] + s[i] == "00": return 0
            if s[i] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

# 结合别人的案例，我自己摸索出来的方法
class Solution1:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        if s[0] == '0': return 0
        dp = [0] * len(s)
        dp[0] = 1
        if len(s) == 1: return dp[-1]
        if s[1] != '0':
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1]+s[i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


# 2020.08.11更新，别人的做法
import functools
class Solution2:
    @functools.lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        ans = 0
        if len(s) >= 1 and s[0] != '0':
            ans += self.numDecodings(s[1:])
        if len(s) >= 2 and s[0] != '0' and int(s[:2]) <= 26:
            ans += self.numDecodings(s[2:])
        return ans


# 这种容易理解一些
class Solution3:
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
            # 考虑两个字母
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

# 2020.08.30 一开始还是没做出来，然后偷偷看了之前的解答
# 经验就是如果是0就跟前面的一样，如果和前面组成两位数，就再加上i-2的值
class Solutionmy:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if s[0] == '0': 
            return 0
        else:
            dp[0] = 1

        if len(s) == 1: return dp[-1]
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            if s[i - 1] + s[i] == "00": return 0
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1] + s[i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

# 2020.09.03 超哥的解法
class Solutionc:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 1
        cnt = 0
        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if 10 <=int(s[0:2])<=26:
            cnt += self.numDecodings(s[2:])
        return cnt
