"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        end_reachable = len(nums) - 1
        for i in range(len(nums)-1, -1 , -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i
        return end_reachable == 0

# 2021.03.23 我的蹩脚的方法，但是有了思路，就能做出来
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        max_index = 0
        size = len(nums)
        for i in range(len(nums)-1):
            if i > max_index:
                return False
            if i + nums[i] >= size -1:
                return True
            max_index = max(max_index, i+nums[i])
        return False

# 2021.03.23 官方解法，从后往前，真是精彩
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        end_reachable = len(nums) - 1
        for i in range(len(nums)-1, -1 , -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i
        return end_reachable == 0
