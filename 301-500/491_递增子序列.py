"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.08.26 我的初始解法，没有跑成功
from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        def backtrack(rest, cur):
            if not rest:
                res.append(cur[:])
            else:
                for i in range(len(rest)):
                    if not cur or cur[-1] <= rest[i]:
                        cur.append(rest[i])
                        backtrack(rest[i+1:], cur)
                        cur.pop()
        
        res = []
        backtrack(nums, [])
        return res

# 覃超老师的解法
class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans, seq = set(), []
        def dfs(i): 
            if len(seq) >= 2:
                ans.add(tuple(seq))
            for j in range(i, len(nums)):
                if len(seq) == 0 or nums[j] >= seq[-1]:
                    seq.append(nums[j])
                    dfs(j+1)
                    seq.pop()
        dfs(0)         
        return list(ans)


# 模仿覃超老师后的改进版
# 注意可用set去重，终止条件优化
class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        def backtrack(rest, cur):
            if not rest:
                res.append(cur[:])
            else:
                for i in range(len(rest)):
                    if not cur or cur[-1] <= rest[i]:
                        cur.append(rest[i])
                        backtrack(rest[i+1:], cur)
                        cur.pop()
        
        res = []
        backtrack(nums, [])
        return res
