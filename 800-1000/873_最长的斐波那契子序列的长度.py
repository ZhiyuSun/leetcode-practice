"""
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：

n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

（回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-longest-fibonacci-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
# 2021.04.04 暴力法
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        S = set(arr)
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                """
                With the starting pair (A[i], A[j]),
                y represents the future expected value in
                the fibonacci subsequence, and x represents
                the most current value found.
                """
                x, y = arr[j], arr[i] + arr[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0



# 2021.04.04 完全看不懂
class Solution1:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(arr):
            for j in range(k):
                i = index.get(z - arr[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0


# 2021.04.04 民间解法
class Solution2:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = {}
        res = 0
        tempA = set(A)
        for i in range(1,len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                if diff <A[j] and diff in tempA:
                    dp[(A[j],A[i])] = dp.get((diff,A[j]),2)+1
                    res = max(res,dp[(A[j],A[i])])
        return res
