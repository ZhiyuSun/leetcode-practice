"""
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections

# 2021.04.15 不行了，题目太简单，我要开始飘了
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = collections.defaultdict(int)
        left = right = res = 0
        while right < len(s):
            dic[s[right]] += 1
            while len(dic) > 2:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res