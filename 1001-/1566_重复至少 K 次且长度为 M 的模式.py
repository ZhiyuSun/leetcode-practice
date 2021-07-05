"""
给你一个正整数数组 arr，请你找出一个长度为 m 且在数组中至少重复 k 次的模式。

模式 是由一个或多个值组成的子数组（连续的子序列），连续 重复多次但 不重叠 。 模式由其长度和重复次数定义。

如果数组中存在至少重复 k 次且长度为 m 的模式，则返回 true ，否则返回  false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.07.03 经过我的辛苦调试，终于做出来了
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)-m):
            print(i)
            count = 0
            while count < k:
                if i+m+m*count > len(arr):
                    break
                if arr[i:i+m]!= arr[i+m*count:i+m+m*count]:
                    break
                count += 1
                if count == k:
                    return True
        return False

# 2021.07.03 学习官方的解法思路
class Solution2:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for l in range(n - m * k + 1):
            offset = 0
            while offset < m * k:
                if arr[l + offset] != arr[l + offset % m]:
                    break
                offset += 1
            if offset == m * k:
                return True
        return False
