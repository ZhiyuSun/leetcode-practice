"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.11 我一开始的蹩脚方法，能实现，但是会超时
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ans = []
        def dfs(path, cur_sum):
            if len(path) == len(nums):
                if cur_sum == S:
                    ans.append(0)
                    return
                else:
                    return
            i = len(path)
            dfs(path+[nums[i]], cur_sum+nums[i])
            dfs(path+[-nums[i]], cur_sum-nums[i])
        dfs([], 0)
        return len(ans)

# 2021.03.11 参考了别人的做法
class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        def dfs(cur, i, d = {}):
            if i < len(nums) and (i, cur) not in d: # 搜索周围节点
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))
        
        return dfs(0, 0)


# 2021.03.11 就用回溯法做，不相信自己做不出来
# 跑不出来
class Solution3:
    def __init__(self):
        self.result = 0

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        self.backtrack(nums, 0, S)
        return self.result
        
    def backtrack(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                self.result += 1
            return

        rest += nums[i]
        self.backtrack(nums, i+1, rest)
        rest -= nums[i]
        self.backtrack(nums, i+1, rest)
        rest += nums[i]