#!/usr/bin/python
# -*- coding: utf-8 -*-

# 我的解答
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            item = nums.pop()
            nums.insert(0,item)
        
# 民间解答
# 1. 插入
class Solution1:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

# 2. 拼接
class Solution2:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

# 利用切片，在执行时间上有很大的提升


# 2021.03.19 我太垃圾了，这道题都做不出来
from typing import List
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

