"""
给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.04 直奔题解，动态规划
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp=dict()
        for n in arr:
            dp[n]=(dp[n-difference] if n-difference in dp else 0)+1
        return max(dp.values())
