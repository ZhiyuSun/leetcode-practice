"""
给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直面积 的宽度。

垂直面积 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直面积 为宽度最大的一个垂直面积。

请注意，垂直区域 边上 的点 不在 区域内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.15 现在看起来，原来是这么简单的一道题，早上真是失了智
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        ans = 0
        print(points)
        for i in range(1, len(points)):
            ans = max(ans, points[i][0] - points[i-1][0])
        return ans

# 2021.04.15 大牛解法，学会用zip
class Solution1:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])
        return max(p2[0] - p1[0] for p1, p2 in zip(points, points[1:]))