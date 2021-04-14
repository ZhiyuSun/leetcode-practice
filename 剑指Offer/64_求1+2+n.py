"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
import functools

# 2021.04.14 简单的一个递归
class Solution:
    @functools.lru_cache()
    def sumNums(self, n: int) -> int:
        if n == 1: return 1
        return self.sumNums(n-1) + n

# 2021.04.14 参考K神，短路效应
class Solution1:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
