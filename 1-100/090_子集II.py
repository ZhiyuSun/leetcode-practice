"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.21 看了一个大神的解法，感觉自愧不如
# https://leetcode-cn.com/problems/subsets-ii/solution/hui-su-suan-fa-by-powcai-6/

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                helper(i+1, tmp + [nums[i]])
        helper(0, [])
        return res