#!/usr/bin/python
# -*- coding: utf-8 -*-

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