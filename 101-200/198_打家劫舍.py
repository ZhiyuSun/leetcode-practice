"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[size - 1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second


# 覃超老师的思路
# a[i][0,1]: 0: 不偷，1：偷
# a[i][0] = Max(a[i-1][0], a[i-1][1])
# a[i][1] = a[i-1][0] + nums[i]
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        a = [[0,0] for _ in range(len(nums))]
        a[0][0] = 0
        a[0][1] = nums[0]
        for i in range(1, len(nums)):
            a[i][0] = max(a[i-1][0], a[i-1][1])
            a[i][1] = a[i-1][0] + nums[i]
        return max(a[-1][0], a[-1][1])


# 2020.08.12 自己写出来了
class Solutionself:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2]+nums[i])
        return nums[-1]

# 2021.02.25 字节面试遇到了，我写的搓搓的
class Solution4:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) < 2: return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

# 2021.03.24 重温这道题，还是写的慢
class Solution5:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        return nums[-1]