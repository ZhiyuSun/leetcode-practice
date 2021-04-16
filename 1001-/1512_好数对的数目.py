"""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-good-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import collections

# 2021.04.16 我的解法，简单点，想法简单点
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res

# 2021.04.16 官方解法，也是我一开始想到的
class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in m.items())
