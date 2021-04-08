"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.10 其实这道题可以很简单，我这个辣鸡
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

# 2021.03.10 挑战解法2。有点绕
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return i

# 2021.03.20 一遍过，我升级了
class Solution3:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# 2021.04.08 温习一下，其实直接覆盖就行了
class Solution4:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i