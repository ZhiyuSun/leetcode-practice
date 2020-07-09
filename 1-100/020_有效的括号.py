class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for k in s:
            if k in map:
                stack.append(k)
            else:
                if not stack: return False
                if map[stack[-1]] == k:
                    stack.pop()
                else:
                    return False

        return False if stack else True
