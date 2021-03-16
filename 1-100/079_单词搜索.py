"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.16 我失败的做法
from typing import List
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         r = len(board)
#         c = len(board[0])
#         res =[]
#         def bfs(path, cur, visited):
#             if path == word:
#                 res.append(path)
#                 return
#             if not word.startswith(path):
#                 return
#             a, b = cur[0], cur[1]
#             for x,y in [(a+1, b), (a-1,b),(a, b+1), (a,b-1)]:
#                 if x < 0 or x >= r or b < 0 or b >c or (x,y) in visited:
#                     continue
#                 visited.add((x,y))
#                 bfs(path+board[x][y], x, y, visited)
#                 visited.remove((x,y))
#         bfs('', )
#         return len(res) > 0


# 2021.03.16 官方题解，非常精彩，典型的回溯题
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False
