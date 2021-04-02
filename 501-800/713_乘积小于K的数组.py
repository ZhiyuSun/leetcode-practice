"""
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
# 2021.04.02 我的做法，前缀和的思路，但是超时了
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        dp = [1] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            dp[i] = dp[i-1] * nums[i-1]
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if dp[j+1] // dp[i] < k:
                    count += 1
        return count

# 2021.04.02 这是真的滑动窗口的解答啊
class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
