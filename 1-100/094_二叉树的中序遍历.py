# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res


# 2020.9.14 补充递归法
class Solutiondg:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def _inorder(node):
            if not node: return
            _inorder(node.left)
            res.append(node.val)
            _inorder(node.right)

        res = []
        _inorder(root)
        return res


# 2021.03.20 磕磕绊绊

class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res