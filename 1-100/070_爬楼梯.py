"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def climbStairs(self, n):
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

class Solution2:
    def climbStairs(self, n: int) -> int:
        result, a, b = 0, 1, 2
        if n == 1: return 1
        if n == 2: return 2
        for _ in range(n - 2):
            result = a + b
            a = b
            b = result
        return result

# 2020.08.09 信手拈来
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        first, second = 1, 2
        for _ in range(3, n+1):
            first, second = second, first + second
        return second

    
 # 2020.10.22 打印步伐
class Solution4:
    def climbStairs(self, n: int) -> int:
        def _dfs(n, res):
            if n < 0: return
            if n == 0: 
                print(res)
                return 
            _dfs(n-1, res+[1])
            _dfs(n-2, res+[2])
        
        _dfs(n, [])


# 2021.03.18 重温经典
class Solution5:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        f1, f2, ans = 1, 2, 0
        for _ in range(2, n):
            ans = f1 + f2
            f1 = f2
            f2 = ans
        return ans


# 2021.03.20 Python的缓存装饰器
import functools
class Solution6:
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
