"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.23 简单题
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0 , len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                return [nums[i], nums[j]]
            elif s < target:
                i += 1
            else:
                j -= 1