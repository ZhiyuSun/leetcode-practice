"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

 

示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.10.16 找个软柿子捏
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [i*i for i in A]
        res.sort()
        return res


# 数组要记得用双指针法
class Solution1:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        
        return ans

# 2021.04.26 犯规法
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])


# 2021.04.26 数组要记得用双指针
class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1
        
        return ans