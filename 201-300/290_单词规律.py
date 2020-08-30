"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 解法同重构字符串
# 2020。08.28 直奔题解
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        t = str.split()
        if len(pattern) != len(t):
            return False
        dct = {}
        for i in range(len(pattern)):
            if pattern[i] not in dct:
                if t[i] in dct.values():
                    return False
                dct[pattern[i]] = t[i]
            else:
                if dct[pattern[i]] != t[i]:
                    return False
        return True
