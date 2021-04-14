"""
数组 A 是 [0, 1, ..., N - 1] 的一种排列，N 是数组 A 的长度。全局倒置指的是 i,j 满足 0 <= i < j < N 并且 A[i] > A[j] ，局部倒置指的是 i 满足 0 <= i < N 并且 A[i] > A[i+1] 。

当数组 A 中全局倒置的数量等于局部倒置的数量时，返回 true 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/global-and-local-inversions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.14 我的做法，超时了
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        count1 = 0
        count2 = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count1 += 1
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    count2 += 1
        return count1 == count2

# 2021.04.14 官方解法，暴力
class Solution2(object):
    def isIdealPermutation(self, A):
        return all(x < A[j]
                   for i, x in enumerate(A)
                   for j in range(i+2, len(A)))


# 2021.04.14 官方解法，记住最小的值
class Solution3:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        N = len(nums)
        floor = N
        for i in range(N-1, -1, -1):
            floor = min(floor, nums[i])
            if i >= 2 and nums[i-2] > floor:
                return False
        return True
