"""
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。

 

示例 1：

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.10.26 我自己的做法，复杂度警告
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            res.append(count)
        return res


# 在参考题解后的做法，巧用计数排序
class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        for i in nums:
            cnt[i] += 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i-1]
        res = []
        for i in nums:
            res.append(0 if i == 0 else cnt[i - 1])
        return res