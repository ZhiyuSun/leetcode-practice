#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def climbStairs(self, n):
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
