"""
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

 

示例 1:

输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.02 哈希法，yyds
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in dic:
                res = max(i-dic[count], res)
            else:
                dic[count] = i
        return res