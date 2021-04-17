"""
我们定义 arr 是 山形数组 当且仅当它满足：

arr.length >= 3
存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-removals-to-make-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import bisect

# 2021.04.17 完全看不懂，直奔题解
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        def LIS(A):
            d = []
            for a in A:
                i = bisect.bisect_left(d, a)
                if i < len(d):
                    d[i] = a
                elif not d or d[-1] < a:
                    d.append(a)
            return d.index(A[-1])

        for i in range(1, n-1):
            l, r = LIS(nums[:i+1]), LIS(nums[i:][::-1])
            if not l or not r: continue
            ans = min(ans, n - 1 - l - r)
        return ans
