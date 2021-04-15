"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

"""
from typing import List

# 我的答案
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in nums:
            if i in result:
                result.remove(i)
            else:
                result.append(i)
        return result[0]


# 官方解答
# 方法1：列表操作
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


# 方法2：哈希表
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

# 方法3：数学
class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


# 方法4 位操作
class Solution4(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a


s = Solution()
single_num = s.singleNumber([1, 2, 2])
print(single_num)


# 2021.04.15 我的解法，数学法
class Solution5:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]
        return nums[-1]