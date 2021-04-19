"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.02 滑动数组，我的方法做出来了，其间磕磕绊绊，但总归能成功了
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        j = 0
        s = 0
        for i in range(len(nums)):
            if i > 0:
                s -= nums[i-1]
            while j < len(nums) and s < target:
                s += nums[j]
                j += 1
            if s >= target:
                res = min(j-i, res)
        return 0 if res == float('inf') else res


# 2021.04.02 官方解法，说实话，这道题还是挺绕的
class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans


# 2021.04.19 用新学的滑动窗口模板给做出来了
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        res = float('inf')
        s = 0
        while right < len(nums):
            s += nums[right]
            while s-nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                res = min(right-left+1, res)
            right += 1
        return 0 if res == float('inf') else res

# 可以再参考下官方的解答，官方完全使用了我的模板，而且更优雅