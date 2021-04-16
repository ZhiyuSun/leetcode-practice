"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
from typing import List
# 2021.04.01 我的做法，但超时了
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return False
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = sum(nums[i:j+1])
                if s == k:
                    res += 1
        return res

# 2021.04.01 前缀和dp，但是也超时了
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return False
        res = 0
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            dp[i+1] = dp[i] + nums[i]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = dp[j+1] - dp[i]
                if s == k:
                    res += 1
        return res

# 2021.04.01 前缀和+哈希，我终于理解了这个方法了
class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc-k]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return count

# 2021.04.01 我自己的方法
class Solution4:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        s = 0
        count = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in dic:
                count += dic[s-k]
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        return count

# 2021.04.02 综合各种方法的优化版
class Solution5:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        acc = count = 0
        for num in nums:
            acc += num
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc-k]
            d[acc] += 1
        return count

# 2021.04.16 温习一下
class Solution6:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        s = res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in dic:
                res += dic[s-k]
            dic[s] += 1
        return res