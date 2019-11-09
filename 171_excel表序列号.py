#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result += (ord(s[i])-64) * (26 ** (len(s)-1-i))
        return result

s = Solution()
print s.titleToNumber('AB')


# 民间算法
# 1行
class Solution1(object):
    def titleToNumber(self, s):
        return sum([(ord(s[i]) - ord('A') + 1)*26**(len(s)-i-1) for i in range(len(s))])

# 另外的简洁的写法
import functools
class Solution2:
    def titleToNumber(self, s):
        return functools.reduce(lambda x, y: x * 26 + y, [ord(a) - 64 for a in s ])


class Solution3:
    def titleToNumber(self, s):
        return sum( (ord(a) - 64) * (26 ** i)  for i, a in enumerate(s[::-1]))
