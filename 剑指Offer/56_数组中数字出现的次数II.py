"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
"""
import collections
from typing import List

# 2021.04.24 我的方法
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k

# 2021.04.24 K神解法，状态转移，真是6
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
