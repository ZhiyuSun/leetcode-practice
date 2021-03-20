"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

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

# 2021.03.20 只要有思路，就不难写
class Solution1:
    def isValid(self, s: str) -> bool:
        bracket_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in bracket_map:
                stack.append(i)
            else:
                if not stack: return False
                top = stack.pop()
                if bracket_map[top] != i:
                    return False
        return False if stack else True

# 官方解法，可以先验证长度
class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack
