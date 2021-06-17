"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

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


# 2020.7.19 重温投票法

class Solution5:
    def majorityElement(self, nums):
        count = 0
        candidate = None


        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


# 2021.03.21 一遍过
from typing import List
class Solution6:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# 2021.06.17 温习一下
class Solution7:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                res = i
            if i == res:
                count += 1
            else:
                count -= 1

        return res