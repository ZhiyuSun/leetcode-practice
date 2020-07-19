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

# 2020.7.19号更新
# 官方解法
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True

# 我的解法
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True