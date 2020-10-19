"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        
        self.backtrack([], nums, check)
        return self.res
        
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            check[i] = 0


# 2002.9.18更新
class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _backtrace(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                _backtrace(sol+[nums[i]])
                check[i] = 0
        
        nums.sort()
        res = []
        check = [0] * len(nums)
        _backtrace([], )
        return res


# 心得整理
# 需要标记每个数是否有被用过