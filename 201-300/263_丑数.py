"""
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.15 我的解法，简单轻松
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False
        for i in [2,3,5]:
            while n % i == 0:
                n = n // i
        return n == 1

# 2021.04.15 官方解法
class Solution1:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        
        return n == 1
