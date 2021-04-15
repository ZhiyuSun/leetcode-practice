"""
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.15 可以说基本掌握滑动窗口的模板了
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = res = count = 0
        while right < len(nums):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right-left)
            right += 1
        return res