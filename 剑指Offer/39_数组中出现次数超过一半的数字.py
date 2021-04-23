"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。


你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

from typing import List

# 2021.04.23 我的解法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                ans = i
            if i == ans:
                count += 1
            else:
                count -= 1
        return ans

# 2021.04.23 K神解法，太美了
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x
