"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。
"""
from typing import List

# 2021.04.15 举一反三，学会滑动窗口
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = right = max0 = 0
        while right < len(A):
            if A[right] == 0:
                max0 += 1
            if max0 > K:
                if A[left] == 0:
                    max0 -= 1
                left += 1
            right += 1
        return right - left

# 2021.04.15 官方解法，一种更易于理解的滑动窗口的思路
class Solution1:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = lsum = rsum = 0
        ans = 0
        
        for right in range(n):
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
