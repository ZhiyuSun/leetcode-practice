"""
给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

示例 1：

输入: "code"
输出: false
示例 2：

输入: "aab"
输出: true
示例 3：

输入: "carerac"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.20 我的解法
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = collections.defaultdict(int)
        for i in s:
            dic[i] += 1
        count = 0
        for v in dic.values():
            if v % 2 == 1:
                count += 1
        return count <= 1