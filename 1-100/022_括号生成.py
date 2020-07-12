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