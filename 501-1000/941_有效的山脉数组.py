"""
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
"""

# 2020.11.4 简单题都要直奔题解，我TM真是太菜了

# 解法1：线性扫描
from typing import List
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1

# 双指针
class Solution2:
    def validMountainArray(self, A):
        length = len(A)
        left, right = 0, length-1
        while left + 1 < length and A[left] < A[left+1]:
            left += 1
        while right > 0 and A[right-1] > A[right]:
            right -= 1
        return left > 0 and right < length-1 and left == right

# 高效方法
class Solution3:
    def validMountainArray(self, A: List[int]) -> bool:
        '''
        if len(A)<3:
            return False
        for i in range(len(A)-1):
            if A[i]>=A[i+1]:
                c = i
                break
            return False
        if c==0:
            return False
        for j in range(c,len(A)-1):
            if A[j]<=A[j+1]:
                return False
        return True
        '''
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1