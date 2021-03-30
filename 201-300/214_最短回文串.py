"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

 

示例 1：

输入：s = "aacecaaa"
输出："aaacecaaa"
示例 2：

输入：s = "abcd"
输出："dcbabcd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.30 直接弃疗，不解释
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base, mod = 131, 10**9 + 7
        left = right = 0
        mul = 1
        best = -1
        
        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + mul * ord(s[i])) % mod
            if left == right:
                best = i
            mul = mul * base % mod
        
        add = ("" if best == n - 1 else s[best+1:])
        return add[::-1] + s
