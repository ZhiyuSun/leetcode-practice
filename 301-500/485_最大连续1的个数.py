"""
给定一个二进制数组， 计算其中最大连续 1 的个数。

 

示例：

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.17 我真是个傻逼
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for _, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        
        maxCount = max(maxCount, count)
        return maxCount


# 2021.03.17 一次遍历就够了
class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res

# 2021.03.17 参考民间大神的双指针解法
class Solution3:
    def findMaxConsecutiveOnes(self, nums):
        index = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                res = max(res, i - index)
        return res
