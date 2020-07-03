#!/usr/bin/python
# -*- coding: utf-8 -*-

# 这题太难了，完全不会


# 民间解答1
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def find(s, k, left, right):
            if left > right:
                return 0
            
            # 用字典存储所有字符出现的情况
            hash_map = dict()
            for i in range(left, right + 1):
                c = s[i]
                if hash_map.get(c, None) == None:
                    hash_map[c] = []
                hash_map[c].append(i)
                
            for key in hash_map.keys():
                # 某个字符出现的次数
                counter = len(hash_map[key])
                # 如果字符出现次数 < k，那么该字符不可能出现在最终要求的子串中，在该字符的位置对原字符串进行截断
                if counter > 0 and counter < k:
                    # 该字符首次出现的位置
                    pos = hash_map[key][0]
                    # 根据该字符的位置对字符串进行截断，判断左右两个截断的字字符哪个更长
                    return max(find(s, k, left, pos - 1), find(s, k, pos + 1, right))
            
            return right - left + 1
        
        return find(s, k, 0, len(s) - 1)

# 民间解答2
class Solution2(object):
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                # 满足分割条件，进行分割
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # 如果每个字符出现的次数均不小于k，则返回当前字符串的长度
        return len(s)
