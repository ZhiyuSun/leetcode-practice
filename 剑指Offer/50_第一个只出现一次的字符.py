"""

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
"""
import collections

# 2021.04.08 太简单了
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.defaultdict(int)
        for i in s:
            dic[i] += 1
        for i in s:
            if dic[i] == 1:
                return i
        return " "
        
# 2021.04.08 K神解法
class Solution1:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '
