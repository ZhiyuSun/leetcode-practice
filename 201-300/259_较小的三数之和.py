"""
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2 
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.19 直奔题解，双指针，注意加值的方式
class Solution:
    def func(self, nums: List[int], L: int, target: int) -> int:    #两个数的和小于target
        res = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] + nums[R] < target:
                res += (R - L)
                L += 1
            else:
                R -= 1
        return res

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n - 2):      #3个数的和，分解成2个数的和  先固定住一个变量，控制变量
            res += self.func(nums, i + 1, target - nums[i])
        return res
