"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

"""

from typing import List

# 我的初始解法，但是在定位行的时候，找到精准的值
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        bottom, top = 0, len(matrix) - 1
        while bottom <= top:
            row_mid = (bottom + top) // 2
            if matrix[row_mid][0] == target:
                return True
            elif matrix[row_mid][0] < target:
                bottom = row_mid + 1
            else:
                top = row_mid - 1
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            col_mid = (left + right) // 2
            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][col_mid] < target:
                left = col_mid + 1
            else:
                right = col_mid - 1
        return False


s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))

# 解法1，虚拟下标
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        #二分查找
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False


# m+n的解法
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (len(matrix) and len(matrix[0])):
            return False
        row, col = 0, len(matrix[0])-1
        while row <= len(matrix)-1 and col >= 0:
            curr = matrix[row][col]
            if curr == target: return True
            if target < curr:
                col -= 1
            else:
                row += 1
        return False