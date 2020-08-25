"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = {}
        needs = {}
        for c in p: needs[c] = needs.get(c, 0) + 1
        length, limit = len(p), len(s)
        left = right = 0

        while right < limit:
            c = s[right]
            if c not in needs:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window.get(c, 0) + 1
                if right - left + 1 == length:
                    if window == needs: res.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return res
