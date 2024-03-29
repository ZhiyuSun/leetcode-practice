"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import functools

# 2021.04.14 我的这个思路绝了，一步一步的探索，直到找到正确答案
class Solution:
    @functools.lru_cache()
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(2, n):
            res = max(res, i * self.cuttingRope(n - i), i * (n-i))
        return res

# 2021.04.14 贪心，数学，不好证明
class Solution2:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res *=3
            n -= 3
        return res * n


# 2021.04.25 我的解法，自己又写出来了，但是居然还跟上次写的不一样
class Solution3:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j] * j, (i-j) * j)
        return dp[-1] % 1000000007

# 2021.04.25 重温官方解法，更精简一点
class Solution4:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n] % 1000000007