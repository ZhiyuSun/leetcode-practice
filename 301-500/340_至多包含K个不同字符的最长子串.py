"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

# 2021.04.19 重温双指针
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