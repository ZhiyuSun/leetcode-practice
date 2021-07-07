"""
我们把符合下列属性的数组 A 称作山脉：

A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

 

示例 1：

输入：[0,1,0]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.24 我的投机取巧法
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i


# 2021.04.24 二分法，想简单点，不需要移动指针时都去加减1
class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo

# 2021.07.07 自己倒腾了一个二分法
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j = 0, len(arr) - 1
        while i < j:
            mid = (i+j) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                i = mid
            if arr[mid-1] > arr[mid] > arr[mid+1]:
                j = mid
        return None

# 2021.07.07 官方解法
# 注意一下这才是标准的二分，判断哪里用=，左右指针+1-1

class Solution3:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
