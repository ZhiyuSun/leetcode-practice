#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def generateMatrix(self, n):
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat


from typing import List

class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        l, r, t, b = 0, n-1, 0, n-1
        num = 1
        while num <= n*n:
            for i in range(l, r+1):
                res[t][i] = num
                num += 1
            t += 1
            for i in range(t, b+1):
                res[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l-1, -1):
                res[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t-1, -1):
                res[i][l] = num
                num += 1
            l += 1

        return res