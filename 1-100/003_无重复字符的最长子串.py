"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""

# 我自己的解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        i = 0
        res = 1
        ch_set = {s[0]}
        for j in range(1, len(s)):
            if s[j] in ch_set:
                while i < j and s[i] != s[j]:
                    ch_set.remove(s[i])
                    i += 1
                i += 1
            ch_set.add(s[j])
            res = max(res, len(ch_set))
        return res

# 民间大神解法
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res