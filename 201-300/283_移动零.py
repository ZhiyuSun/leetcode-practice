# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        for k in range(j, len(nums)):
            nums[k] = 0
        return nums

# 优化后
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


# 2020.11.24 花了三天，终于写出来了，一雪前耻。
# 最巧妙的还是上一个方法
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        i, j = 0, 1
        while j < len(nums) and i < len(nums):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    j += 1
            else:
                i += 1
                j += 1
        return nums

# 2021.03.16 我这也太6了吧，这居然自己做出来了
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        return nums