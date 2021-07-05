"""
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 线性查找
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1


# 递归二分查找
def search(nums, l, r):
    if l == r:
        return l
    mid = (l + r) / 2
    if nums[mid] > nums[mid + 1]:
        return search(nums, l, mid)
    return search(nums, mid + 1, r)

class Solution1(object):
    def findPeakElement(self, nums):
        return search(nums, 0, len(nums) - 1)


# 迭代二分查找
class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


# 2021.07.05 很普通的做法，比较垃圾
class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        if len(nums) < 2:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
