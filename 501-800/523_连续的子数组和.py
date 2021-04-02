"""
给定一个包含 非负数 的数组和一个目标 整数 k ，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n * k ，其中 n 也是一个整数。

 

示例 1：

输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：

输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.01 我的做法，可以做出来，但是超时了
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s = sum(nums[i:j+1])
                if s == 0 or s % k == 0:
                    return True
        return False

# 2021.04.01 学习官方题解，前缀和的思路，但还是超时了
class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp = [0] * (len(nums)+1)
        dp[0] = nums[0]
        for i in range(1, len(nums)+1):
            dp[i] += dp[i-1] + nums[i-1]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s = dp[j+1] - dp[i]
                if s == 0 or s % k == 0:
                    return True
        return False


# 2021.04.01 前缀和优化，借助哈希表
# 设位置 j < i : 
# 0 到 j 的前缀和 preSum1 = 某常数1 * k + 余数1
# 0 到 i 的前缀和 preSum2 = 某常数2 * k + 余数2
# 当找到 余数1 等于 余数2时， 则 j + 1 到 i 的连续和 = preSum2 - preSum1 = (某常数2 - 某常数1) * k， 必为 k 的倍数， 返回true

# 2021.04.01 我的前缀和+哈希表解法，利用到了余数的特点
class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        dic = {}
        s = 0
        dic[0] = -1
        for i in range(len(nums)):
            s += nums[i]
            r = s % k
            if r in dic:
                if i - dic[r] > 1:
                    return True
            else:
                dic[r] = i
        return False


# 这个用例有待讨论：
# [1,0,0,0]
# 2
# 这是正确的用例，0可以被2整除


# 2021.04.01 同余定理
class Solution3:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        dp, cur = {0: -1}, 0
        for idx, num in enumerate(nums):
            cur += num
            if k != 0: cur %= k
            pre = dp.setdefault(cur, idx)
            if idx - pre > 1: return True
        return False

