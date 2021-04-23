"""
统计一个数字在排序数组中出现的次数。
"""
from typing import List

# 2021.04.23 过于简单
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)


# 2021.04.23 排序数组，二分法的思路值得学习
class Solution1:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)
