"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))