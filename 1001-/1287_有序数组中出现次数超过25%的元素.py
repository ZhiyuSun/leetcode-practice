"""
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数

 

示例：

输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import defaultdict

# 2021.04.08 我的解法
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        dic = defaultdict(int)
        count = size // 4
        for i in arr:
            dic[i] += 1
            if dic[i] > count:
                return i
        return -1

# 2021.04.08 要注意到有序的性质，无需开辟字典空间
class Solution1:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cur, cnt = arr[0], 0
        for i in range(n):
            if arr[i] == cur:
                cnt += 1
                if cnt * 4 > n:
                    return cur
            else:
                cur, cnt = arr[i], 1
        return -1

import bisect
# 2021.04.08 有序数组可联想到二分查找，没看懂
class Solution2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            if iter_r - iter_l >= span:
                return arr[i]
        return -1
