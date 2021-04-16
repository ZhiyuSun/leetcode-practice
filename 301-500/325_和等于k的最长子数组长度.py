"""
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。

注意:
 nums 数组的总和是一定在 32 位有符号整数范围之内的。

示例 1:

输入: nums = [1, -1, 5, -2, 3], k = 3
输出: 4 
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:

输入: nums = [-2, -1, 2, 1], k = 1
输出: 2 
解释: 子数组 [-1, 2] 和等于 1，且长度最长。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.02 我的做法，灵活运用前缀和+哈希，牛逼啊
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = -1
        res = s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in dic:
                res = max(res, i-dic[s-k])
            if s not in dic:
                dic[s] = i
        return res

# 2021.04.02 为了写题解，做的暴力法
class Solution2:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    res = max(res, j-i+1)
        return res


# 2021.04.03 为了写题解，做的前缀和
class Solution3:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0
        dp = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            dp[i] += dp[i-1] + nums[i-1]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = dp[j+1] - dp[i]
                if s == k:
                    res = max(res, j-i+1)
        return res

# 2021.04.16 前缀和+哈希表，还好没忘记
class Solution4:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dic = {0: -1}
        s = res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in dic:
                res = max(i-dic[s-k], res)
            if s not in dic:
                dic[s] = i
        return res
