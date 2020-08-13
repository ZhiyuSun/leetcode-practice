"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13

"""

class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        a, b, c = 1, 2, 4
        for _ in range(3, n):
            a, b, c = b, c, (a+b+c) % 1000000007
        return c 


# 打印所有的解法
class Solutiondfs:
    def waysToStep(self, n: int) -> int:
        steps = [1, 2, 3]
        self._dfs(n, [], steps)

    def  _dfs(self, n , res, steps):
        if n == 0:
            print(res)
            return
        for step in steps:
            if n >= step:
                self._dfs(n-step, res+[step], steps)


# 打印所有解法，并且相邻的步长不能重复
class Solutionnorepeat:
    def waysToStep(self, n: int) -> int:
        steps = [1, 2, 3]
        self._dfs(n, [], steps, 0)

    def  _dfs(self, n , res, steps, last_step):
        if n == 0:
            print(res)
            return
        for step in steps:
            if n >= step and step != last_step:
                self._dfs(n-step, res+[step], steps, step)