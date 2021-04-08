"""
给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
如果可以，请返回 True；否则，返回 False。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List

# 2021.04.08 这道题没什么深文大义，纯粹是把自己的思路能够用算法表达出来就行
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        while count:
            m = min(count)
            for i in range(m, m+k):
                v = count[i]
                if not v: return False
                if v == 1:
                    del count[i]
                else:
                    count[i] = v - 1

        return True

# 2021.04.08 另一种思路
class Solution1:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        s = collections.Counter(nums)
        ordered_nums = sorted(s)
        for num in ordered_nums:
            occ = s[num]
            if s[num] > 0:
                for i in range(num + 1, num + k):
                    if s[i] >= occ:
                        s[i] -= occ
                    else:
                        return False
        return True
