
#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections
# 我的答案
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table[i] = hash_table[i] + 1
            except:
                hash_table[i] = 1
        arr_length = len(nums)
        for key,value in hash_table.items():
            if value > arr_length/2:
                return key

s = Solution()
single_num = s.majorityElement([1, 2, 2])
print(single_num)


# 官方解答
# 1.暴力法
class Solution1:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

# 2.哈希表
class Solution2:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# 3.排序
class Solution3:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


# 4.Boyer-Moore投票算法
class Solution4:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
