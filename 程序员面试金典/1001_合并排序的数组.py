"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sorted-merge-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



# 2020.10.15 直奔题解，非常有挫败感
from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] < B[pb]:
                sorted.append(A[pa])
                pa += 1
            else:
                sorted.append(B[pb])
                pb += 1
        A[:] = sorted



# 逆向双指针
class Solution2:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pa, pb = m - 1, n - 1
        tail = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1
