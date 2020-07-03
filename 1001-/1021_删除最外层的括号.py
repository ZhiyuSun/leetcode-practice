class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        stack = []
        for i in S:
            if i == ')':
                stack.pop()
                if len(stack) > 0:
                    result += ')'
            else:
                stack.append(i)
                if len(stack) > 1:
                    result += '('
        return result
