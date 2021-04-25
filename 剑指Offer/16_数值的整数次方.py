"""

实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
"""
import functools

# 2021.04.25 一开始的做法，可惜失败了
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            isBelowZero = True
            n = -n
        else:
            isBelowZero = False

        @functools.lru_cache()
        def _my_pow(x, n):
            if n == 1:
                return x
            res = self.myPow(x, n//2) * self.myPow(x, n//2)
            if n % 2 == 1:
                res *= x
            return res

        res = _my_pow(x, n)
        if isBelowZero:
            return 1 / res
        else:
            return res

# 2021.04.25 K神解法，值得好好赏析，很巧妙
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

# 2021.04.25 正确的递归解法
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n & 1:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x*x, n // 2)

# 2021.04.25 我的修改版，感觉lru失效了，有风险，面试时最好不要使用
class Solution3:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            isBelowZero = True
            n = -n
        else:
            isBelowZero = False

        def _my_pow(x, n):
            if n == 1:
                return x
            res = self.myPow(x*x, n // 2)
            if n & 1:
                res *= x
            return res

        res = _my_pow(x, n)
        if isBelowZero:
            return 1 / res
        else:
            return res