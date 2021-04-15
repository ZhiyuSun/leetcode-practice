"""
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keys-and-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List

# 2021.04.15 我的BFS解法
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        queue = rooms[0]
        while queue:
            print(queue)
            key = queue.pop(0)
            visited.add(key)
            for i in rooms[key]:
                if i not in visited:
                    queue.append(i)
        return len(rooms) == len(visited)


# 2021.04.15 官方解法BFS
class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        num = 0
        vis = {0}
        que = collections.deque([0])

        while que:
            x = que.popleft()
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    vis.add(it)
                    que.append(it)
        
        return num == n


# 2021.04.15 官方解法DFS
class Solution2:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        
        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n
