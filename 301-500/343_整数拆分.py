"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import functools
# 2021.04.14 小试牛刀
class Solution:
    @functools.lru_cache()
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(2, n):
            res = max(res, i * self.integerBreak(n - i), i * (n-i))
        return res

# 2021.04.14 官方解法，动态规划
class Solution1:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
