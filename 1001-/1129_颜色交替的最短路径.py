"""
在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。

red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

 

示例 1：

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
示例 2：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
示例 3：

输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]
示例 4：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]
示例 5：

输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-with-alternating-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.10 直接弃疗
from typing import List
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_path = [set() for i in range(n)]
        blue_path = [set() for i in range(n)]
        dist = [[None, None] for i in range(n)]
        dist[0] = [0, 0]
        step = 0
        now_red = [0]
        now_blue = [0]
        for start, end in red_edges:
            red_path[start].add(end)
        for start, end in blue_edges:
            blue_path[start].add(end)
        # step 1 找到分别以红边开始和以蓝边开始的两条最短路径
        while len(now_red) != 0 or len(now_blue) != 0 :
            new_red, new_blue = [], []
            step += 1
            if len(now_blue) != 0:
                for point in now_blue:
                    for next_point in red_path[point]:
                        if dist[next_point][0] is None:
                            new_red.append(next_point)
                            dist[next_point][0] = step
            if len(now_red) != 0:
                for point in now_red:
                    for next_point in blue_path[point]:
                        if dist[next_point][1] is None:
                            new_blue.append(next_point)
                            dist[next_point][1] = step
            now_red, now_blue = new_red, new_blue
        # step 2 在这两条最短路径中选择小的，merge成我们的答案
        ans = []
        for i in range(n):
            if dist[i][0] is None and dist[i][1] is None:
                ans.append(-1)
            elif dist[i][0] is not None and dist[i][1] is not None:
                ans.append(min(dist[i][0], dist[i][1]))
            elif dist[i][0] is not None:
                ans.append(dist[i][0])
            else:
                ans.append(dist[i][1])
        return ans
