"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 官方解法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


# 模仿覃超老师的写法
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def _generate(left, right, n, s):
            if left == n and right == n:
                res.append(s)
                return
            
            if left < n:
                _generate(left+1, right, n, s+"(")

            if left > right:
                _generate(left, right+1, n, s+")")

        
        res = []
        _generate(0, 0, n, "")
        return res

s = Solution2()
print(s.generateParenthesis(3))

# 某一天我自己的写法
class Solution3:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def traceback(i, j, ans):
            if i > n or j > i: return 
            if i == n and j == n: 
                res.append(''.join(ans))
                return
            ans.append('(')
            traceback(i+1, j, ans[:])
            ans.pop()
            ans.append(')')
            traceback(i, j+1, ans[:])
        
        traceback(0, 0, [])


        return res

# 队列法
class Solution4:
    def generateParenthesis(self, n: int) -> List[str]:
        res, queue = [], []
        queue.append(('',n,n))
        while queue:
            path, left, right = queue.pop(0)
            if left == right == 0:
                res.append(path[:])
                continue
            if left > 0: queue.append((path+'(', left-1, right))
            if right > left: queue.append((path+')', left, right-1))
        return res


# 2020.08.27
class Solutionmy:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrace(left, right, cur):
            if left == 0 and right == 0:
                res.append(cur)
                return
            if left > 0:
                backtrace(left-1, right, cur+'(')
            if left < right:
                backtrace(left, right-1, cur+')')

        res = []
        backtrace(n, n, '')
        return res


# 2020.11.15 用递归的方法，顺利写出来了，但其实多用了一些变量
class Solution5:
    def generateParenthesis(self, n: int) -> List[str]:
        def _dfs(left_num, right_num, left_count, right_count, cur):
            if left_num == 0 and right_num == 0:
                res.append(cur)
                return
            if left_num > 0:
                _dfs(left_num-1, right_num, left_count+1, right_count, cur+"(")
            if right_num > left_num:
                _dfs(left_num, right_num-1, left_count, right_count+1, cur+")")
        
        res = []
        _dfs(n, n, 0, 0, "")
        return res

# 优化版
class Solution6:
    def generateParenthesis(self, n: int) -> List[str]:
        def _dfs(left_num, right_num, cur):
            if left_num == 0 and right_num == 0:
                res.append(cur)
                return
            if left_num > 0:
                _dfs(left_num-1, right_num, cur+"(")
            if right_num > left_num:
                _dfs(left_num, right_num-1, cur+")")
        
        res = []
        _dfs(n, n, "")
        return res