"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

"""
class Solution(object):
    def solveNQueens(self, n):
        def valid(row, col, track):
            if col in track:  # 判列
                return False
            for k in range(row):  # 判斜对角
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False
            return True

        def backtrack(row, track):
            if row == n:  # 已到最后一行
                res.append(track)
                return
            for col in range(n):
                if valid(row, col, track):  # 若位置合法，则进入下一行
                    backtrack(row + 1, track + [col])

        res = []
        backtrack(0, [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in l] for l in res]


# 2021.03.21 直奔题解
class Solution2:
    def solveNQueens(self, n):
        def valid(row, col, track):
            if col in track:  # 判列
                return False
            for k in range(row):  # 判斜对角
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False
            return True

        def backtrack(row, track):
            if row == n:  # 已到最后一行
                res.append(track)
                return
            for col in range(n):
                if valid(row, col, track):  # 若位置合法，则进入下一行
                    backtrack(row + 1, track + [col])

        res = []
        backtrack(0, [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in l] for l in res]

# 2021.03.30 要额外记录track的路径
