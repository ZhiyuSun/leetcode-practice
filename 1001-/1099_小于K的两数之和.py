"""
给你一个整数数组 nums 和整数 k ，返回最大和 sum ，满足存在 i < j 使得 nums[i] + nums[j] = sum 且 sum < k 。如果没有满足此等式的 i,j 存在，则返回 -1 。

 

示例 1：

输入：nums = [34,23,1,24,75,33,54,8], k = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
示例 2：

输入：nums = [10,20,30], k = 15
输出：-1
解释：
我们无法找到和小于 15 的两个元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.22 两数之和
from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans, N = -1, len(nums)
        left, right = 0, N - 1
        nums.sort()
        while left < right:
            S = nums[left] + nums[right]
            if S < k:
                ans = max(ans, S)
                left += 1
            else:
                right -= 1
        return ans 
