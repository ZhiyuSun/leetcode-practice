"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n-1) == 0


# 2021.03.29 太轻松了
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n-1) == 0

# 2021.03.29 迭代法
class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
