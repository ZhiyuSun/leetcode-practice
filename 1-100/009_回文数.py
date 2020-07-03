#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        s = str(x)
        begin,end = 0, len(s)-1
        while begin < end:
            if s[begin] == s[end]:
                begin += 1
                end -= 1
            else:
                return False
        return True