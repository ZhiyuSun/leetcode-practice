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

class Solution2:
    def climbStairs(self, n: int) -> int:
        result, a, b = 0, 1, 2
        if n == 1: return 1
        if n == 2: return 2
        for _ in range(n - 2):
            result = a + b
            a = b
            b = result
        return result

# 2020.08.09 信手拈来
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        first, second = 1, 2
        for _ in range(3, n+1):
            first, second = second, first + second
        return second