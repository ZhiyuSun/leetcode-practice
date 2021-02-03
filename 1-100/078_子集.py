"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

# 回溯
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

# 2020.08.28 惨败，还是不会


# 2021.02.03 还是不会，参考旧的解法
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _dfs(first, cur, k):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(first, len(nums)):
                cur.append(nums[i])
                _dfs(i+1, cur, k)
                cur.pop()
        
        res = []
        for k in range(len(nums) + 1):
            _dfs(0, [], k)
        return res

# 另一种解法，利用python可以巧妙的转化回溯
class Solution4:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _dfs(first, cur, k):
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(first, len(nums)):
                _dfs(i+1, cur + [nums[i]], k)
        
        res = []
        for k in range(len(nums) + 1):
            _dfs(0, [], k)
        return res