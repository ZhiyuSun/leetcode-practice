"""
给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

示例 1：

输入：[1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

# 2021.04.15 请叫我双指针的神
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)
        left = right = res = 0
        while right < len(s):
            dic[s[right]] += 1
            while len(dic) > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res
