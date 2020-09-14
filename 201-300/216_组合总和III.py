"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def _dfs(n, k, start, cur):
            if n < 0 or k < 0: return
            if k == 0 and n == 0:
                res.append(cur[:])
                return
            for i in range(start, 10):
                cur.append(i)
                _dfs(n-i, k-1, i+1, cur)
                cur.pop()
        res = []
        _dfs(n, k, 1, [])
        return res
