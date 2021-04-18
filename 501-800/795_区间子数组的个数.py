"""
给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。

求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。

例如 :
输入: 
A = [2, 1, 4, 3]
L = 2
R = 3
输出: 3
解释: 满足条件的子数组: [2], [2, 1], [3].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-subarrays-with-bounded-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.18 秀的我头皮发麻
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        def count(bound):
            ans = cur = 0
            for x in A :
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)

# count的意思是小于等于bound的子数组的个数