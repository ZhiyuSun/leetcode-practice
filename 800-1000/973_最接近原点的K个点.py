"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2020.11.09 我真是越来越没用了，垃圾
from typing import List
import heapq
# 方法1：排序
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

# 方法2：优先队列
class Solution1:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)
        
        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans


# 2021.04.26 温习一下
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)
        
        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            if q[0][0] < dist:
                heapq.heappop(q)
                heapq.heappush(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans