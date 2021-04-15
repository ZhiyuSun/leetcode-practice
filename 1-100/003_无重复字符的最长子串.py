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

# 2021.01.26 我好笨，曾经会做的题现在不会了
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


# 2021.02.21 我TMD真是个垃圾，做过的题，现在重做花了一小时
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        window_set = set()
        res = 0
        while j < len(s):
            if s[j] not in window_set:
                window_set.add(s[j])
                res = max(res, j-i+1)
            else:
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        break
                    else:
                        window_set.remove(s[i])
                        i += 1
            j += 1
        return res


# 2021.04.15 所谓成长，就是在不断超越，我终于做出来了
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = res = 0
        visited = set()
        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res
