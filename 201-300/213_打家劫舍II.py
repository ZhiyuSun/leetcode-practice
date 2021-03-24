"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return sum(nums)
        a, b, c, d = 0, 0, 0, nums[0]
        for i in nums[1: -1]:
            a, b, c, d = b, max(b, a+i), d, max(d, c+i)
        return max(b, a+nums[-1], d)


# 2021.03.24 去掉首来一遍，去掉尾来一遍
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.rob_2(nums[1:]), self.rob_2(nums[:-1]))

    def rob_2(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        return nums[-1]