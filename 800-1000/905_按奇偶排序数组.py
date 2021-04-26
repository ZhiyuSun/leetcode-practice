"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

 

示例：

输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.26 我的解法，活用lambda表达式
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)

# 2021.04.26 官方解法，两边扫描
class Solution1:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])

# 2021.04.26 官方双指针
class Solution2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A

# 2021.04.26 我的双指针，似乎更复杂了
class Solution3:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while 0 <= i < j < len(A):
            while A[i] % 2 == 0 and i < len(A)-1:
                i += 1
            while A[j] % 2 == 1 and j > 0:
                j -= 1
            if 0 <= i < j < len(A):
                A[i], A[j] = A[j], A[i]
        return A
