"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""

# 2020.12.7 我就只能找软柿子捏了
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([0] * (i+1))
        for level in range(1, numRows):
            cur = res[level]
            before = res[level-1]
            for i in range(level+1):
                if i - 1 >= 0:
                    cur[i] += before[i-1]
                if i < level:
                    cur[i] += before[i]
        return res

# 官方简洁法

class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret
