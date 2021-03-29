"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        return len(res)

class Solution1:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_not_under_attack(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col])
        
        def place_queen(row, col):
            rows[col] = 1
            hills[row - col] = 1  # "hill" diagonals
            dales[row + col] = 1  # "dale" diagonals
        
        def remove_queen(row, col):
            rows[col] = 0
            hills[row - col] = 0  # "hill" diagonals
            dales[row + col] = 0  # "dale" diagonals
        
        def backtrack(row = 0, count = 0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count
        
        rows = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        return backtrack()

# 2021.03.27 哇塞，我自己居然做出来了，牛逼！
class Solution2:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        col, pie, na = set(), set(), set()
        def _dfs(level):
            if level == n:
                self.res += 1
                return
            for j in range(0, n):
                if j in col or level + j in pie or level -j in na:
                    continue
                col.add(j)
                pie.add(level +j)
                na.add(level-j)
                _dfs(level + 1)
                col.remove(j)
                pie.remove(level +j)
                na.remove(level-j)

        _dfs(0)
        return self.res