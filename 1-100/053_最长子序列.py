"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""

# 2020.11.24 复习一下
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)

# 2021.03.24 我自己想出了另一种思路
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# 2021.03.24 变体
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            res = max(res, nums[i])
        return res
