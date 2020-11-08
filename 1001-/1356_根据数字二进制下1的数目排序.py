"""
给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。

如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。

请你返回排序后的数组。

 

示例 1：

输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import defaultdict as d

# 2020.11.08 退步太多，直奔题解
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = d(list)

        for i in arr:
            c = 0
            for s in str(bin(i)):
                if s == "1":
                    c += 1
            dic[c].append(i)

        output = []
        for j in range(15):
            if dic[j]:
                for temp in sorted(dic[j]):
                    output.append(temp)

        return output
