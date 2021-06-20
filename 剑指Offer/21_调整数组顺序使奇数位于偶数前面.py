"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.12.25 我自己想的方法1，冒泡排序的思路，很挫的方法
from typing import List
class Solution1:
    def exchange(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] % 2 == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

# 灵机一动，双指针法
class Solution2:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 1:
                i+=1
                continue

            if nums[j] % 2 == 0: 
                j -=1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# 学习别人的快慢指针法
class Solution3:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums

# 2021.06.20 我用双指针自己做出来了
class Solution4:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums