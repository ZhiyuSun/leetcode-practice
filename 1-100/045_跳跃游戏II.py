"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""
from typing import List

# 超出时间限制
class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps

# 顺藤摸瓜
class Solution1:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        max_position, end, step = 0, 0, 0
        for i in range(size-1):
            max_position = max(max_position, i+nums[i])
            if i == end:
                end = max_position
                step += 1
        return step