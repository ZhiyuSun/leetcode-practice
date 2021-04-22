"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.22 我的解法
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0: return False
        seen = set()
        for i in nums[0:k+1]:
            if i in seen:
                return True
            seen.add(i)
        i = 0
        for j in nums[k+1:]:
            seen.remove(nums[i])
            i += 1
            if j in seen:
                return True
            seen.add(j)
        return False

# 2021.04.22 参考民间解法，这解法太妙了
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}    
        for i in range(len(nums)):
            if nums[i] in dct and dct[nums[i]] >= i-k:
                return True
            dct[nums[i]] = i
        return False