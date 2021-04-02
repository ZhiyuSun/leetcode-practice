"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List

# 递归解法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        result = [root.val]
        for child_root in root.children:
            result.extend(self.preorder(child_root))
        return result

# 迭代解法
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output

# 2021.03.18 参考二叉树的解法
class Solution3:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            for i in reversed(tmp.children):
                stack.append(i)
        return res
