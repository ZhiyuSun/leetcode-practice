"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""
# 2020.08.12 我的投机取巧的方法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# 2020.08.12 自己想用双指针，辛苦写了很多，结果超出了时间限制
class Solutionszz:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(haystack) < len(needle): return -1
        haystack_length = len(haystack)
        needle_length = len(needle)
        for i in range(haystack_length):
            k = i
            for j in range(needle_length):
                if haystack[k] != needle[j]:
                    break
                if j == needle_length-1: return i
                k += 1
                if k == haystack_length: break
        return -1

# 官方解答，子串逐一比较
class Solutionzc:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1