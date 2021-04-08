"""
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数
"""

from typing import List
from collections import defaultdict

# 2021.04.08 我的解法，没啥说的

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        dic = defaultdict(int)
        count = size // 4
        for i in arr:
            dic[i] += 1
            if dic[i] > count:
                return i
        return -1
