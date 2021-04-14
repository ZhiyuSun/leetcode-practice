"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021.04.14 这题有点容易啊
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        def mirror(node):
            node.left, node.right = node.right, node.left
            if node.left:
                mirror(node.left)
            if node.right:
                mirror(node.right)
        mirror(root)
        return root

# 2021.04.14 K神的解法
class Solution1:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

# 2021.04.14 K神的解法，BFS
class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
