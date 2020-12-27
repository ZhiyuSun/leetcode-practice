"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 怎么做都做不出的解法
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch_map = {}
        temp = []
        i = 0
        while i < len(s):
            if s[i] == t[i]:
                if s[i] not in ch_map:
                    temp.append(s[i])
                    i += 1
                else:
                    return False
            else:
                if s[i] in temp or t[i] in temp:
                    return False

                if s[i] in ch_map:
                    if ch_map[s[i]] != t[i]:
                        return False
                    else:
                        i +=1
                else:
                    ch_map[s[i]] = t[i]
                    i += 1
        return True


# 别人的答案
class Solution2:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=t[i]
            else:
                if dic[s[i]]!=t[i]:
                    return False
        return True

# 我的修改版
class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch_map = {}
        i = 0
        while i < len(s):
            if s[i] in ch_map:
                if ch_map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in ch_map.values():
                    return False
                else:
                    ch_map[s[i]] = t[i]
            i += 1
        return True


class Solution4:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map_dict_a = {}
        map_dict_b = {}
        for i in range(len(s)):
            if s[i] in map_dict_a:
                if t[i] != map_dict_a[s[i]]:
                    return False
            else:
                map_dict_a[s[i]] = t[i]
            if t[i] in map_dict_b:
                if s[i] != map_dict_b[t[i]]:
                    return False
            else:
                map_dict_b[t[i]] = s[i]
        return True