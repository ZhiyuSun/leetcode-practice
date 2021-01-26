"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# 第一版，我写了一个返回值的版本，因为字节面试的时候遇到了
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            return None
        nums.sort()
        i, j = 0, len(nums)-1
        while i < j:
            result = nums[i] + nums[j]
            if result == target:
                return [nums[i], nums[j]]
            elif result < target:
                i += 1
            else:
                j -= 1
        return None

# 第二版，暴力法。时间复杂度O(n2),空间复杂度O(1)
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
        return None

class Solution2:
    def twoSum(self, nums, target):
        data_dict = dict()
        for i, element in enumerate(nums):
            if target - element in data_dict:
                return [data_dict[target-element], i]
            data_dict[element] = i


a = Solution2()
print(a.twoSum([1,2,3], 3))


# 2020.12.30 而今迈步从头越
from typing import List
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 2021.01.16 终于会使用字典了
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in data_dict.keys():
                return [i, data_dict[target - nums[i]]]
            else:
                data_dict[nums[i]] = i
        
