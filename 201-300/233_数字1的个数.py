"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

 
"""

# 2021.04.24 直奔题解，是我看不懂的题目
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res
