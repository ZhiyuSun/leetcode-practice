"""
有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。

对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。

并返回一个包含给定查询 queries 所有结果的数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xor-queries-of-a-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.17 我的前缀和的思路
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [0] * (len(arr)+1)
        s = 0
        for i in range(len(arr)):
            s ^= arr[i]
            dp[i+1] = s
        res = []

        for i in queries:
            res.append(dp[i[0]] ^ dp[i[1]+1])

        return res

# 2021.04.17 我的优化版
class Solution1:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [0] * (len(arr)+1)
        for i in range(len(arr)):
            dp[i+1] = dp[i] ^ arr[i]
        res = []

        for i in queries:
            res.append(dp[i[0]] ^ dp[i[1]+1])

        return res

class Solution2:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for num in arr:
            pre.append(pre[-1] ^ num)
        ans = list()
        for x, y in queries:
            ans.append(pre[x] ^ pre[y + 1])
        return ans
