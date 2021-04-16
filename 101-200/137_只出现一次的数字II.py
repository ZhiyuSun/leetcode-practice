"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

 

示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.16 没想到位运算的解法，于是直奔题解
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2


# 2021.04.16 hashmap
from collections import Counter
class Solution1:
    def singleNumber(self, nums):
        hashmap = Counter(nums)
            
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k


from typing import List
# 2021.04.16 位运算，但是我看不懂
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
