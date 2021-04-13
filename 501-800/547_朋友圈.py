"""
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2 
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friend-circles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# dfs 方法
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(visited, j)
        
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(visited, i)
                count+=1
        return count

# 并查集, 有点不太好懂
class Solution1:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)
        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x=i
            i=p[i]
            p[x]=root
        return root

# 2021.04.13 我自己写出了并查集
class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(i):
            if parent[i] != i:
                return find(parent[i])
            return i

        def union(i, j):
            rooti = find(i)
            rootj = find(j)
            parent[rooti] = rootj
        parent = []
        for i in range(len(isConnected)):
            parent.append(i)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] != 0:
                    union(i, j)
        s = set()
        for i in parent:
            s.add(find(i))
        return len(s)
