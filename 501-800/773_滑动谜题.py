"""

在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.

一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.

最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
"""
# 2021.03.30 直奔题解
from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbor = {0: [1, 3], 1:[0, 2, 4], 2:[1, 5],
                    3:[0, 4], 4:[3, 1, 5], 5:[4, 2]}
        start = ''
        target = '123450'
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
            
        queue = [start]
        visited = set()
        visited.add(start)
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == target:
                    return step
                idx = cur.index('0')
                for near in neighbor[idx]:
                    new = self.swap(cur, idx, near)
                    if new not in visited:
                        queue.append(new)
                        visited.add(new)
            step += 1
        return -1

    def swap(self, cur, i, j):
        cur_list = list(cur)
        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
        return "".join(cur_list)

