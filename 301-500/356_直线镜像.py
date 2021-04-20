"""
在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y 轴的直线，让这些点关于这条直线成镜像排布？

注意：题目数据中可能有重复的点。
"""
from typing import List

# 2021.04.20 没看懂，随便炒一个答案
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if len(points) == 0:
            return True
        points = sorted(points,key = lambda x:x[1])
        pre = points[0][1]
        l = 0
        n = len(points)
        flag = 0
        for i in range(n):
            if i == n-1 or points[i+1][1] != pre:
                nums = []
                for j in range(l,i+1):
                    nums.append(points[j][0])
                if flag == 0:
                    m = max(nums)+min(nums)
                    flag = 1
                for num in nums:
                    if m - num not in nums:
                        return False
                if i < n-1:
                    pre = points[i+1][1]
                l = i + 1
        return True
