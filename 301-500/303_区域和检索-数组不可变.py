"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.05 自己摸索，使用面积的思路
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            dp[i+1] = dp[i] + nums[i]
        print(dp)
        self.dp = dp

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]


# 2021.03.05 官方解答
class NumArray2:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]

