#!/usr/bin/python
# -*- coding: utf-8 -*-

# 我的解答
class Solution(object):
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            while i < len(s)-1 and not s[i].isalnum():
                i += 1
            while j > 0 and not s[j].isalnum():
                j -= 1
            if i > j:
                return True
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True


# 民间解答
class Solution1:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > -1 and not s[j].isalnum():
                j -= 1
            if i > j:
                return True
            if s[i].upper() != s[j].upper():
                return False
            else:
                i += 1
                j -= 1
        return True

# 重点是python的isalnum方法，判断字符串是数字或数组