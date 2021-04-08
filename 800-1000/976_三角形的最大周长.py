"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。
"""
from typing import List

# 2021.04.08 我自己的解法，数学+贪心法
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)-2):
            if nums[i+1]+ nums[i+2] > nums[i]:
                return nums[i+1]+ nums[i+2] + nums[i]
        return 0

# 2021.04.08 民间大神解法，要注意sort可以直接接reverse排序
class Solution1:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0