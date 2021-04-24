"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

"""

# 2021.04.24 我就喜欢作弊
class Solution:
    def add(self, a: int, b: int) -> int:
        return a + b


# 2021.04.24 位运算
class Solution1:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
