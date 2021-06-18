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


# 2021.04.12 我在成长，我在变化，用到了最远距离的思路
class Solution4:
    def canJump(self, nums: List[int]) -> bool:
        max_d = nums[0]
        for i in range(len(nums)):
            if i > max_d:
                return False
            if max_d >= len(nums) - 1:
                return True
            max_d = max(max_d, nums[i] + i)


# 2021.06.18 我做出来了，但是不够优雅
class Solution5:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True

# 2021.06.18 回顾官方解法，从前往后
class Solution6:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
