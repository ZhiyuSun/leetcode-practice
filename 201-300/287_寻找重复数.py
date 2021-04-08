"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

 

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
# 2021.04.08 真的是简单的题吗
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for i in nums:
            dic[i] += 1
        for k, v in dic.items():
            if v > 1:
                return k


# 2021.04.08 原地处理的思路很厉害
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[abs(nums[i])]<0:return abs(nums[i])
            nums[abs(nums[i])] = - nums[abs(nums[i])]

# 2021.04.08 不要忘了set法
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)
