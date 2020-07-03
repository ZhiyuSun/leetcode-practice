#!/usr/bin/python
# -*- coding: utf-8 -*-

# 线性查找
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1


# 递归二分查找
def search(nums, l, r):
    if l == r:
        return l
    mid = (l + r) / 2
    if nums[mid] > nums[mid + 1]:
        return search(nums, l, mid)
    return search(nums, mid + 1, r)

class Solution1(object):
    def findPeakElement(self, nums):
        return search(nums, 0, len(nums) - 1)


# 迭代二分查找
class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


