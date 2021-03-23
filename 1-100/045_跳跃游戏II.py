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

# 2021.03.09 做过的题都不会做了，辣鸡
class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # maxPos：目前能跳到的最远位置
        # end：上次跳跃可达范围右边界（下次最右起跳点）
        # step：跳跃次数
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i: # 其实这个判断非必须
                maxPos = max(maxPos, i + nums[i])
                # 到达上次跳跃能到达的右边界了
                if i == end:
                    # 目前能跳到的最远位置变成了下次起跳位置的右边界
                    end = maxPos
                    # 进入下一次跳跃
                    step += 1
                    # 优化：起跳点达到或者超过终点就可以结束循环了
                    if maxPos >= len(nums) - 1:
                        break

        return step
# 有点难以理解
# 思想就一句话：每次在上次能跳到的范围（end）内选择一个能跳的最远的位置（也就是能跳到max_far位置的点）作为下次的起跳点 ！

# 2021.03.23 我自己的动态规划，居然做出来了，虽然有点蹩脚
class Solution3:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            max_index = i + nums[i]
            for j in range(i, max_index+1):
                if j < len(nums):
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

# 2021.03.23 另一种解法，从结尾开始，每次找到能走到的最远的点
class Solution4:
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
