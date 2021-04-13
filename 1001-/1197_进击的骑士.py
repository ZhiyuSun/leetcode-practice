"""
一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。

骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格。

每次移动，他都可以按图示八个方向之一前进。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-knight-moves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
# 2021.04.13 我的解法，BFS
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = collections.deque()
        direction = [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]
        queue.append((0,0, 0))
        visited = {(0, 0)}
        while queue:
            i, j, count = queue.popleft()
            if i == x and j == y:
                return count
            for di, dj in direction:
                if (i+di, j+dj) not in visited:
                    queue.append((i+di, j+dj, count+1))
                    visited.add((i+di, j+dj))

# 2021.04.13 稍微优化了一下，提了个速
class Solution2:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = collections.deque()
        direction = [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]
        queue.append((0,0, 0))
        visited = {(0, 0)}
        while queue:
            i, j, count = queue.popleft()
            current_length = abs(y - j) + abs(x - i)
            if i == x and j == y:
                return count
            for di, dj in direction:
                ni, nj = i+di, j+dj
                length = abs(y - nj) + abs(x - ni)
                if (ni, nj) not in visited and (length <= current_length or current_length <= 3):
                    queue.append((ni, nj, count+1))
                    visited.add((ni, nj))
